from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.components.health_check import generate_health_check
from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
async def read_root() -> dict:
    """
    Lê o endpoint raiz e retorna o nome do proprietário.

    :return:
    Um dicionário/json com o @ do owner.

    :rtype: dict
    """
    return {'owner': '@machadoah'}


@app.get('/health', status_code=HTTPStatus.OK, response_model=Message)
async def health_check() -> dict:
    """
    Verifica o estado da API e retorna uma mensagem
    indicando se está funcionando corretamente.

    :return:
    Uma mensagem gerada por um modelo de linguagem (LLM).

    :rtype: dict
    """
    return {'message': generate_health_check()}
