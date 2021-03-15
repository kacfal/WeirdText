from fastapi import FastAPI
from pydantic import BaseModel

from weird_text import WeirdText

app = FastAPI(version='v1')


class Text(BaseModel):
    text: str


@app.post('/encode')
def get_encode_text(input_text: Text):
    return Text(text=WeirdText().encode(text=input_text.text))


@app.post('/decode')
def get_decode_text(input_text: Text):
    return Text(text=WeirdText().decode(text=input_text.text))
