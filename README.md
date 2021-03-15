# WierdText

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

### Requirements
```
python >= 3.7
```
### Installing

After installing Python and pip just call:

```
pip install -r requirements.txt
```

to start dev server simply:

```
uvicorn api.endpoints:app --reload
```


## Running the tests

```
python -m pytest tests/
```

## API Documentation

```
http://127.0.0.1:8000/docs
```