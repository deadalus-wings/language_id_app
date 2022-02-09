# imports

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import fasttext

# DONE: Input arbitrary text
# Done: Detect Language of the text
# ONGOING: Web application front end to accept text and display language
# ONGOING: 2 meaningful unit tests
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



templates = Jinja2Templates(directory="static")


@app.get("/", response_class = HTMLResponse)
async def home_write(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

@app.post("/submitform")
async def handle_form(fname : str=Form(...)):
    model = fasttext.load_model("id_lang.bin")
    language_id = model.predict(fname)
    language_id_key = language_id[0][0]
    language_detected = language_dictionary[language_id_key]
    # return templates.TemplateResponse("homepage.html", {"request": Request})
    return language_detected

@app.get("/")
async def root():
    return {"data": "test"}

