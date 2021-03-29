from fastapi import FastAPI, Response
from pydantic import BaseModel

from weird_text import WeirdText
from weird_text.exceptions import DecodingException

app = FastAPI(version='v1')


class Text(BaseModel):
    text: str


@app.post('/encode')
def encode(input_text: Text):
    """ Accepts string text and returns encoded string text. """
    return Text(text=WeirdText().encode(text=input_text.text))


@app.post('/decode')
def decode(input_text: Text):
    """ Accepts encoded string text, tries decode it and returns. """
    return Text(text=WeirdText().decode(text=input_text.text))


@app.exception_handler(DecodingException)
async def exception_handler(request, exc):
    return Response(str(exc), status_code=400)
