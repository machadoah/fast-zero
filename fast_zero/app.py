from http import HTTPStatus

from fastapi import FastAPI

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'owner': '@machadoah'}
