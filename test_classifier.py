import unittest
import classifier

class TestStringMethods(unittest.TestCase):

    def test_csv_to_txt(self):
        input_file = "valid.csv"
        text_file = classifier.csv_to_txt(input_file)
        self.assertEqual(text_file, "valid.txt")

    def test_organise_data(self):
        input_file = "land_id_train"
        resultant_file_name = classifier.organise_data(input_file)
        self.assertEqual(resultant_file_name,"land_id_train.txt")
        with open(resultant_file_name, 'r') as f:
            output = f.readline()
            self.assertEqual(output[:9],"__label__")

    def test_train_model(self):
        input_file = "land_id_train.txt"
        model = classifier.train_model(input_file)
        self.assertTrue(len(model.get_labels()), 20)


if __name__ == '__main__':
    unittest.main()