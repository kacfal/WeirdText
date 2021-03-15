from fastapi import FastAPI
from pydantic import BaseModel

from weird_text import WeirdText

app = FastAPI(version='v1')


class Text(BaseModel):
    text: str


@app.post('/encode')
def encode(input_text: Text):
    """ Gets string text and returns encoded string text. """
    return Text(text=WeirdText().encode(text=input_text.text))


@app.post('/decode')
def decode(input_text: Text):
    """ Gets encoded string text, tries decode it and returns. """
    return Text(text=WeirdText().decode(text=input_text.text))

