import fasttext
import csv
import re

# mock_input =

def csv_to_txt(input_file):
    resultant_text_file = "csv_to_text.txt"
    with open(resultant_text_file, "w") as my_output_file:
        with open(input_file, "r") as my_input_file:
            [my_output_file.write(" ".join(row) + '\n') for row in csv.reader(my_input_file)]
        my_input_file.close()
        my_output_file.close()
    return resultant_text_file



def organise_data(input_file):
    data_file = open(input_file, "r")
    datalines = data_file.readlines()
    rows = datalines[1:]
    resultant_file_name = data_file.name+".txt"
    resultant_file = open(resultant_file_name,"w")
    for i in rows:
        lang_text = i.partition(',')[2].replace('"','').replace('(','').replace(')','')
        # result = ''.join([j for j in lang_text if not j.isdigit()])
        result = re.sub(r'[0-9]+', '', lang_text)
        result = ' '.join(result.split())
        print(result)

        d = "__label__"+str(i.partition(',')[0])+" "+result.lower()+"\n"
        # print(d)
        resultant_file.write(d)

    resultant_file.close()
    data_file.close()
    return resultant_file_name

def train_model(input_file):
    model = fasttext.train_supervised(input=input_file, lr=1, epoch=25, wordNgrams=2)
    model.save_model("id_lang.bin")
    # print(model.test("csv_to_text.txt.txt"))
    # model.test("test.csv")
    return model

validation_txt = csv_to_txt("valid.csv")
training_data = organise_data("land_id.train")
validation_data = organise_data("csv_to_text.txt")
model = train_model(training_data)
print(model.test("csv_to_text.txt.txt"))
print(model.predict("ότι", k=-1, threshold=0.5))