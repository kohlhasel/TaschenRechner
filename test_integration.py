import ast

import pytest

from flaskus import create_app, APP


@pytest.fixture
def client():
    app = APP
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

# def test_version_string(client):
#     """Wenn die Version abgefragt wird, dann soll die aktuelle Version zurückgegeben werden (version: 67.0 -- Lukas Kohlhase)"""
#     #Arrange
#
#     #Act
#     result = client.get('/version')
#     #Assert
#     data = ast.literal_eval(result.data.decode().strip())
#     assert data['version'] == '67.0 -- Lukas Kohlhase'


def test_addition(client):
    """Wenn Addition abgefragt wird, dann kommen plausible Werte raus"""
    #Arrange
    post_data = dict(wert1='3', wert2='7')
    #Act
    result = client.post('/add', json=post_data)
    #Assert
    data = result.data.decode()
    assert data == '10'

def test_addition_bug(client):
    """Wenn Addition abgefragt wird, dann kommen plausible Werte raus"""
    #Arrange
    post_data = dict(wert1='0.666', wert2='1')
    #Act
    result = client.post('/add', json=post_data)
    #Assert
    data = result.data.decode()
    assert data == '1.666'

def test_subtraktion(client):
    """Wenn Subtraktion abgefragt wird, dann kommen plausible Werte raus"""
    #Arrange
    post_data = dict(wert1='8', wert2='7')
    #Act
    result = client.post('/sub', json=post_data)
    #Assert
    data = result.data.decode()
    assert data == '1'

def test_multiplikation(client):
    """Wenn Subtraktion abgefragt wird, dann kommen plausible Werte raus"""
    #Arrange
    post_data = dict(wert1='8', wert2='7')
    #Act
    result = client.post('/mul', json=post_data)
    #Assert
    data = result.data.decode()
    assert data == '56'