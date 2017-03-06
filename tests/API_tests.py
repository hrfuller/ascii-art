import requests
import os

test_url = "http://localhost:5000/"

artify_endpoint = test_url + 'artify'


def test_no_file():

    r = requests.post(artify_endpoint)

    assert r.status_code == 400


def test_no_post():
    r = requests.get(artify_endpoint)

    assert r.status_code == 405


def test_wrong_file_type():
    non_image = open(os.path.dirname(__file__) + '/fixtures/non-image', 'rb')
    r = requests.post(artify_endpoint, files={'file': non_image})

    assert r.status_code == 400


def test_succesful_art():
    image = open(os.path.dirname(__file__) + '/fixtures/image', 'rb')
    r = requests.post(artify_endpoint, files={'file': image})

    assert r.status_code == 200
    art_json = r.json()
    assert 'art' in art_json
