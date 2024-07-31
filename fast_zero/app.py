from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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


@app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
async def read_root_html() -> str:
    """
    Lê o endpoint raiz e retorna o nome do proprietário.

    :return:
    Um dicionário/json com o @ do owner.

    :rtype: str
    """
    return """
    <html>
        <head>
            <title>Fast-Zero :zap:</title>
        </head>
        <body>
            <h1>@machadoah</h1>
        </body>
    </html>
    """


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
