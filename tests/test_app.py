from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_owner():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmação)
    assert response.json() == {'owner': '@machadoah'}  # Assert (Afirmação)


def test_read_root_deve_retornar_ok_e_owner_em_html():
    client = TestClient(app)

    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <html>
        <head>
            <title>Fast-Zero :zap:</title>
        </head>
        <body>
            <h1>@machadoah</h1>
        </body>
    </html>
    """
    )


def test_health_check_deve_retornar_ok_e_mensagem():
    client = TestClient(app)

    response = client.get('/health')

    assert response.status_code == HTTPStatus.OK
    assert 'API' in response.json()['message'].upper()
