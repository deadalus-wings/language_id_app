# imports
from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import fasttext
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# TODO: Input arbitrary text
# TODO: Detect Language of the text
# TODO: Web application front end to accept text and display language
# TODO: 2 meaningful unit tests
# app = FastAPI()
language_dictionary_flipped = {
    "arabic": "__label__ar", "bulgarian" : "__label__bg",
    "german": "__label__de", "modern greek": "__label__el",
    "english": "__label__en", "spanish" : "__label__es",
    "french": "__label__fr", "hindi": "__label__hi",
    "italian": "__label__it", "japanese": "__label__ja",
    "dutch": "__label__nl", "polish": "__label__pl",
    "portuguese": "__label__pt", "russian": "__label__ru",
    "swahili": "__label__sw", "thai": "__label__th",
    "turkish": "__label__tr", "urdu": "__label__ur",
    "vietnamese": "__label__vi", "chinese": "__label__zh"
}
language_dictionary = dict(map(reversed, language_dictionary_flipped.items()))

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"))


templates = Jinja2Templates(directory="static")


@app.get("/", response_class = HTMLResponse)
async def home_write(request: Request):
    # return HTMLResponse(content ="homepage.html", status_code=200)
    return templates.TemplateResponse("homepage.html", {"request": request})

@app.post("/submitform")
async def handle_form(fname : str=Form(...)):
    model = fasttext.load_model("id_lang.bin")
    language_id = model.predict(fname)
    language_id_key = language_id[0][0]
    language_detected = language_dictionary[language_id_key]
    return {language_detected}

@app.get("/")
async def root():
    return {"data": "test"}





# @app.get('/query/')
# async def detect_spam_query(message: str):
#    return classify_message(model, message)

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#
#     return {"model_name": model_name, "message": "Have some residuals"}