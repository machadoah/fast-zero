from http import HTTPStatus


def test_read_root(client):
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmação)
    assert response.json() == {'message': '@machadoah'}  # Assert (Afirmação)


def test_create_user(client):
    response = client.post(
        url='/users/',
        json={
            'username': 'machadoah',
            'password': 'password',
            'email': 'machado@ah.com',
        },
    )

    # RETORNOU 201?
    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        'username': 'machadoah',
        'id': 1,
        'email': 'machado@ah.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'users': [{'id': 1, 'username': 'machadoah', 'email': 'machado@ah.com'}]}


def test_read_user(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'id': 1, 'username': 'machadoah', 'email': 'machado@ah.com'}


def test_read_user_not_found(client):
    response = client.get('/users/98')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found 💥',
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'machadoah.tech',
            'password': 'senha',
            'email': 'machado@machadoah.tech',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'machadoah.tech',
        'id': 1,
        'email': 'machado@machadoah.tech',
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/98',
        json={
            'username': 'machadoah.tech',
            'password': '<PASSWORD>',
            'email': 'machado@machadoah.tech',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found 💥',
    }


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User 1 deleted 🗑️'}


def test_delete_user_not_found(client):
    response = client.delete('/users/98')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found 💥',
    }
