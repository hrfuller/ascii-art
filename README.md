# ascii-art
Flask JSON API to convert images into ASCII art

Installing dependancies
------------------------------------------------

1. Install `python-pip` from your package manager
    * Debian: `sudo apt-get install python-pip`
    * Redhat: `sudo yum install python-pip`
    * OSX: `brew install python-pip`
2. Install virtualenv: `pip install virtualenv`
3. Initialize a virtualenv in toplevel ascii_art directory:
`virtualenv ./`
4. Activate the virtualenv
`source bin/activate`
5. Install package requirements 
`pip install -r requirements.txt`

Running Test Server
------------------------------------------------
1. Setup Flask environment variables:
    * `export FLASK_APP=ascii_art/ascii_art.py`
2. Move to directory containing this README
3. Start virtualenv: `source bin/activate`
4. Run Flask server: `flask run`

The server should now be running on `localhost:5000`

Running Production Server
------------------------------------------------

We can use Gunicorn to run multiple workers of our app.
For example:

`gunicorn -w 4 -b 127.0.0.1:4000 ascii_art.ascii_art:app`

Of course the number of workers and port binding can be configured
as desired.

Using the API
------------------------------------------------

This simple API has only one endpoint.

Endpoint | Methods | Accepts                                   | 200 JSON
---------|---------|-------------------------------------------|--------------
/artify  | POST    | mutlipart file upload with one key: "file" | '{"art": "ascii-art-string"}'

###Return Values:

*200*: On success a JSON object with one key `art` whose value is the ASCII art
string is returned. The ascii string is scaled to a maximum width or height of 256
characters, while the aspect ratio is maintained. The string is newline
seperated, where each line represents one row of the rasterized image from top
to bottom.

*400*: If there was a problem with the uploaded file, a BAD REQUEST status is
returned and an error message is passed in the response body.

###Example (requires cURL):

`curl -X POST --form file=@/location/of/image/file.png localhost:5000/artify`

A simple UI is provided for ASCII-ifying and viewing pleasure. Simply navigate
to `localhost:5000/` in your browser to use.

###Example using Python requests:

```python
>>> import requests
>>> url = 'http://localhost:4000/artify'
>>> image = open('tests/fixtures/image', 'rb')
>>> response = requests.post(url, files={'file': image})
>>> response.status_code
200
>>> print r.json()['art']
jrxxrxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxrj
xnnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunnx
nuuuvvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuun
xnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvnx
xnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvnx
xnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvnx
xnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunnnnnnxxnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunnnnnuvvvvcvzvuvuununuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunnunuvvuzUJJL0CQLJJzvuunnuvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunnuvcY0Ompdddbdwqdmmdbbbddp0Lzvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunxxvYQwmppmQLLJUYYXXzzzXXYYUCZwdpZLXuxunuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunncXULZqpwm0CzuuxjfrjjjjjjjjrrxXLZwwmOCXunuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunvzUZqpZ0JvxjjjrjrrrrrrrrrrrrrrrrjjjxcUmqw0CYvnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunvU0pqOCurrjrrrrrrrrrrrrrrrrrrrrrrrxrrrrxzLkdwXunuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuuuuuuuuuvuunxvUOdOQYcnrjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjxuJLZwQcnnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuuuuuuuuuuuxuCkdZUcnrrrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrxvCmpmYnnuvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuuuuuuuuunnXQqdOYjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrnYwdmXuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuuuuuunnuzCqpOnjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjnYqwLJunuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuuuuuunuzZamzxjrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrjjxmkdcnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuuuuuuxvZdmcxrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjjrcCmwCcxuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuuuunnLwOXnjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrv0hpcnuvvvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuuuunUqdXrfrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjfzwdLzvnunuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuunncddCrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrruCd0zxuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuuuuunUdmzjrrxrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrjxJdqzxuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunx
xnuuuuuuuuuuuuuuununYOpzxjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjnJqZYnnnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunr
xnuuuuuuuuuuuuuuunuvOqCfjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrxCpZXnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunj|
xnuuuuuuuuuuuuuuuuvOqLrrrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrfCmmzvnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuur|[+
xnuuuuuuuuuuuuuunvJpJxxrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrzmZXxvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvuunj|-++
xnuuuuuuuuuuuuuunYwwvjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrxYbZYnuvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvvn/1?+++
xnuuuuuuuuuuuuuxcOpUrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrJwqXnnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvf)?_+__+
xnuuuuuuuuuuuuunUq0urrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrxQp0vnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuxf{?++__++
xnuuuuuuuuuuuunv0dcrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrvLwCcuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuxt[-_____++
xnuuuuuuuuuuuunLZUrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjuOdCunuvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvun/{-+______++
xnuuuuuuuuuuuuuppujjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjxUZqzxvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuux\[-_________+
xuuuuuuuuuuuuxXkqrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrnUdLvnuuuvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvnj\[++_________+
xnuuuuuuuuuunnQZYjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrxCpZunuunuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuux/]_+___________+
xnuuuuuuuuuuucZCurrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrxjrbkXnnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuux|[+_+___________+
txuuuuuuuuvuvYqUrrxrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrfQqQnnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunj)?_~_____________+
-)jvuuuuuuvxc0mcrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrjxCdCcxxnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunr)]_++______________+
~?1fuuuuuuvxYwOurrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjzmq0JXcuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuf(?+++_______________+
~++{jnuuuuunJdQnrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrxXdbdwUcnnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuf1-+__________________+
+++_}|xuuunuLbUjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrxnzOdwzxuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuj)?+++__________________+
++++_?(juunv0bYjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrcYO0Unuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu\}?______________________+
~+++++?)juncmpzjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjjrjrjnUqZvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuxf[++______________________+
+++++++_[tfzmmcrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrQqCuxuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuxt)?+________________________+
++++++++_}\vZQcrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrnurjrrrrrrrrrfcQwvnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuux/]++_________________________+
~++++++++-?fZCurjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrQOcrrrrrrrrjrjrJdYvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuf([__+_________________________+
~++_++_++_~(ZCurjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrUpwnjrrrrjrrjrjzwJvnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuj|[-~+-__________________________+
~++++++++++|ZJurrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrruOoQzrjrrrjjrjfvZLvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunt(]++__-__________________________+
~+++++++++~|ZJujrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjxuvrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrxu0M*dQJXccccccvYmOznuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuj\[_+_______________________________+
~+++++++++~)OJujrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjvCZrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrLpp0woobwmwwmmOmkZznnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvut{?+__-______________________________+
~+++++++++<1CLurrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrfcZdrrrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrr0mXccQ0OqpqpppdkabLuxuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvunvuj[-++_________________________________+
~+++++++_+~}JOzrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrf0pZjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjvurjjrxnzcccvvzYULw0Xnuvvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuut1?++___________________________________+
~+++++++_+<[UwYjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrpamvrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjjjrrjjrjfffffffrvQp0vuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunf}_++____________________________________+
~+++++++_++_vdUjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrckWkLvfrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrrxrrrrjrrrrjrxnmpJnnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuxt{_+_+-___________________________________+
~+++++++++++jqCxjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrzbop0UnrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjvZocnnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvuuj{-+++______________________________________+
~++++++++++~\ZLnjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjfUpaLcunrrjrrrrrrrrrrrrrrrrrrrrrrrjrrrrrrrrrrrrrrrrrrrrrrrrrYdCvxuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvux|}-__________________________________________+
~++++++++++~)J0vjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrzq*wnfjrrrrrrrrrrrrrrrjjrrrrrrrrrxxrrrrrrrrrrrrrrjjjrrrrrrrfuLwYxuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvunx|[_++_________________________________________+
~++++++++++~]nZzjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrcQdpLujjrrrrrrrrrrrrrrrunrxrrjrrrrrzCcrjrjrjrrjrrrxrrrrrrrrrjfrubLvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuur|}_++___________________________________________+
~++++++++++~-\OUrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjjxwobXrjrjrjrrrrrrrrrrrjuLUnjjrrrrjjn0dXrrrrrrrrrxxxuuuuuuuxxxxjjxbOzxuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuux|?_+_+___________________________________________+
~++++++++++++]LQnjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjuC*qUrjjrrrrrrrrrrrrrrrrx0qLfrjrrrjjvwqzrrjrrxcUOmmwqmwbbwwqqw0Yvr0OJnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvvj)]_+__+___________________________________________+
~++++++++++++~rqQjrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjYw*CvjrrrrrrrrrrrrrrrrrrrxuphJrjrrrrjUhLurrcmwqmLCvf\)zp%&*v\rxJqqqddOxuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuur|]-_________________________________________________+
~++++++++++++~1mmjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrxwadxfrrrrrrrrrrrrrrrrrrrrjfJdpvrrrrrrJkXuzJQwOUu/1+!:^{08&o[:i>{nYLpoqnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuut)?~__________________________________________________+
~+++++++++++++_CmnjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrxUadujrrrrrrrrrrrrrrrrrrrrrrrxChJurrrrxJwzzwdwr[!`'`. .'+c&Md~....`,~Yhduuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvuuunj?-_+__________________________________________________+
~++++++++++++++tCLrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrXbOcjrrrrrrrrrrrrrrrrrrrrjrrrjnOdUxrrruQhkbn-".' ... .  "-LC(^ .. .  ,nZvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunj)?_++___________________________________________________+
~++++++++++++++)zmxrjjrrrrrrrrrrrrrrrrrrrrrrjrrjfcmkUrjrrrrrrrrrrrrrjjjjrxuzJQQL0d*OxrrruQ#qx>".          .,~~;'       `x0vuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunuunt{?+______________________________________________________+
~++++++++++++++-rwYnjjrrrrrrrrrrrrrrrrrrrrrrjrrjrCawufrrrrrrrjrrrrjjrnzYUJL0mmO00wawujrjxQhu< ..    ..              .. `jQzuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvuuur\}_~+______________________________________________________+
~+++++++++++++++}LqXjjrrrrrrrrrrrrrrrrrrrrrrrrrjuqkXjrjrrrrrrjjjxucUCQZZOYzuj\)}}\vZXjrjrCO+^. .            ...     .  `f0Xuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunf}_++________________________________________________________+
~++++++++++++++~_rdJrjjrrrrrrrrrrrrrrrrrrrrrrrrjUdQujrrjrrjrrrrrcCmhdZc/}I"`````'"+LUrrrjY0}:..                        ^cqvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvuuux\{-+__________________________________________________________+
~+++++++++++++++~|mmujrrrrrrrrrrrrrrrrrrrrrrrrru0bcxrrrrrjjfrcCmba#hL(i;".       .lUJrrrjX0\I .                       .:Yquuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuun1]-++__________________________________________________________+
~++++++++++++++++?tZYrrrrrrrrrrrrrrrrrrrrrrrrrjQpQrjrrrrjjvLddCubM8#m+           .IYLurrjv0L- ..                      .+YOuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuj|}__+__+_________________________________________________________+
~+++++++++++++++++?UQujrrrrrrrrrrrrrrrrrrrrrrrfwbzxrjrfjuY0Zmz(~Xa%Mw_           .:zLurrrxLdt^..                      '|CQnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuux(]++_-____________________________________________________________+
~+++++++++++++++++-jOLrrrrrrrrrrrrrrrrrrrrrrrrrwpvjrrjruCdpX1:.')mWkX>            ^cLurrrjYdJi                        `z0Cnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunr|?+________________________________________________________________+
~+++++++++++++++++__mkcrjrrrrrrrrrrrrrrrrrrrjruqqujrrnJaqu!^.  .`<1]I'           .IYCnrrrrxUa\^.                     ^+qJuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvux)?+++________________________________________________________________+
~+++++++++++++++++_<cwZrjjrrrrrrrrrrrrrrrrrrjrcpwrjjYOwn}l'. .   `:,'  .         .ILLrrjrrrnmC1`                    .!u0znuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuxt)?++__________________________________________________________________+
~++++++++++++++++++~)XkurjrrrrrrrrrrrrrrrrrrjrcbqrjcmmX>^                      . `>OLjjrrrjrYpU~ .....       .. ..  ;(OXuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunuuvux\}-+____________________________________________________________________+
~+++++++++++++++++++~)C0crrrrrrrrrrrrrrrrrrrrrubpnUmU{" .                      . ;|OYrrrrrrrfCpZ<^ ..        ..   .;cmQvuvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvuurt)-++_____________________________________________________________________+
~++++++++++++++++++_+?\dUrjrrrrrrrrrrrrrrrrrjrxwmJd0~..                          >zmcrrrrrrrrxL*z>'...       . ..."|hkXnnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuun\[_+_-_____________________________________________________________________+
~+++++++++++++++++++~~]mQcjrrrrrrrrrrrrrrrrrrjrZhdp(` .                         .+OOurrrrrrrrjvLhQ("           ..~rOkpLxnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunj|?_+_+_+____________________________________________________________________+
~+++++++++++++++++++++_twprjrrjrrrrrrrrrrrrrrrj0hO[" .                          `/hLrrrrrrrrrrjxLo*U|+,'     ^I}nwwQU0punuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvx1]-+__________________________________________________________________________+
~+++++++++++++++++++__+]CdcrjrjrrrrrrrrrrrrrrrjYwX;...                          IYbUjrrrrrrrjrrxx0hawX(]_<>>])fUZdCuxCkcuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvj|-+++__________________________________________________________________________+
~+++++++++++++++++++++++)Y0nrrrrrrrrrrrrrrrrjrrxJC-". .                        ^{pUnxrrrrxrrrrrrrfum*W*dmJCQphpOUjrfjXdXuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunt[++_____________________________________________________________________________+
~+++++++++++++++++++++++-rmYxrrrrrrrrrrrrrrrrrrrYZz> .                     .   _cdvjjrrrrrrrrrrrrrrz0a*pLCLLYvnrjrjrjzmUvnvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvvuvuxt}_+______________________________________________________________________________+
~+++++++++++++++++++++++~)ZwcrrrrrrrrrrrrrrrrrjjuZd)...                     . `cpUrjrrrrrrrrrrrrrrjrvUdhpUcuxrjrjrrrjv00znvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvvx)]-++______________________________________________________________________________+
~+++++++++++++++++++++++~_rm0nrrrrrrrrrrrrrrrrrrjXqO< .                     'Itq0rfrrrrrrrrrrrrrrrrrrrcCmhpCxffjjrrrjvQpYnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunuuj\}_+++_______________________________________________________________________________+
~++++++++++++++++++++++++~}XZcrjjrrrrrrrrrrrrrrrrnUb\;.                    'i\00cjrrrrrrrrrrrrrrrrrrrrfxYphdQYurrrrrjuQdYxvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvuuuuuj)[_+__________________________________________________________________________________+
~++++++++++++++++++++++++~-|OCrjjrrrrrrrrrrrrrrrxjnZ0/". .                .:rwmcrrrrrrrrrrrrrrrrrrrrrrrrrnCb*b0nxrrjjuJZzxuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvvuuuunt{_+____________________________________________________________________________________+
~+++++++++++++++++++++++++~+vqLrrrrrrrrrrrrrrrrrrrjrmdLl`               .`?zh0vrrrrrrrrrrrrrrrrrrrrrrrrrjrrrYwoapUurjvLZzxuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuj{-+__+___________________________________________________________________________________+
~+++++++++++++++++++++++++++1mwujrrrrrrrrrrrrrrrrrrxzLwY[;             .;r0qCurrrrrrrrrrrrrrrrrrrrrrrrrjrjrrxvJZqbbOzYZOznuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvvn/{-_+_+____________________________________________________________________________________+
~++++++++++++++++++++++++++++UwUrjrrrrrrrrrrrrrrrrrrjvCqU|l,... .  ..^i?fZdOuvcxrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrcCpkdZwbOcxnuuvuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuux|{-_________________________________________________________________________________________+
~+++++++++++++++++++++++++++~)zqxrrrrrrrrrrrrrrrrrrjrjjXmdJr}_~i!><?{/QdbUnrYbZujrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjjrvUqkhwLYcnnuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvrf1_+__________________________________________________________________________________________+
~+++++++++++++++++++++++++++~+twJxrrrrrrrrrrrrrrrrrrrrrrnYwpqOUxxcUOwdqLurjnmoOxrrrrrrrrrrrrrrrrrrrrrrrrrrrrrxrxrjjrncJbdqLcnxuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvn)]-_+__________________________________________________________________________________________+
~++++++++++++++++++++++++++++<{JwcjrrrrrrrrrrrrrrrrrrrrjrnXUCOOO00QQQUzvjjnJhZzrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrrruYU0bmJuxuunuuuuuuuuuuuuuuuuuuuuuuuuuuuur|-_++___________________________________________________________________________________________+
~+++++++++++++++++++++++++++++_{dCxrrrrrrrrrrrrrrrrrrrrrrjrrxuczccunxrrjjzwkOurjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjxxnUQwOYnnuuuuuuuuuuuuuuuuuuuuuuuuuuvx(]-+__+___________________________________________________________________________________________+
~+++++++++++++++++++++++++++++~+OZYfrrrrrrrrrrrrrrrrrrrrrrrrrjjjjjjjjrrxcmkdcrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrc0wOJnuuuuuuuuuuuuuuuuuuuuuuuuunr|?++_______________________________________________________________________________________________+
~++++++++++++++++++++++++++_+++~cqZfrjrrrrrrrrrrrrrrrrrrrxrjrrrrjjrrxruYm*mzjrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrxu0pdcnuuuuuuuuuuuuuuuuuuuuuuuut{?+++-_+____________________________________________________________________________________________+
~+++++++++++++++++++++++++++++++-YwvrjrrrrrrrrrrrrrrrrrrrrrrrjrrxxxuX0hMbvrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrcQdLcnuuvuuuuuuuuuuuuuuuunj|-+___________________________________________________________________________________________________+
~++++++++++++++++++++++++++++++++\UQrjrrrrrrrrrrrrrrrrrrrrrruXUYLOmwqkwLXrrjrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrxcmq0nnuuuuuuuuuuuuuuuuuu/1?++___________________________________________________________________________________________________+
~++++++++++++++++++++++++++++++++]nwurrxrrrrrrrrrrrrrrrrrrrrcOwZqpdqwmXxjrrrrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrYwwYuuuuuuuuuuuuuuuuvxf{-______________________________________________________________________________________________________+
~+++++++++++++++++++++++++++++++++\wLvjxrrrrrrrrrrrrrrrrrrrru0OQLJXvxrfjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjjjrrrrrrrc0qCvuuvuuuuuuuununt)-________________________________________________________________________________________________________+
~++++++++++++++++++++++++++++++++~}LbXjrrrrrrrrrrrrrrrrrrrrrrrxrrrrxrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrrrrjrrrrjjrzppUuuvuuuuuuuuunt[-+_-______________________________________________________________________________________________________+
~++++++++++++++++++++++++++++++++~+ndCjjrrrrrrrrrrrrrrrrrrrrrrrrrjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjjjjrrrrrjrjxCqOcuuuuuuuuuur\}_____+_____________________________________________________________________________________________________+
~+++++++++++++++++++++++++++++++++~1UOvjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrxYurjrjrrrrrjxYq0vxuuuuuux/[-____________________________________________________________________________________________________________+
~++++++++++++++++++++++++++++++++++]jZYjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrxm0cjjrrrrrrrru0mCuuuuuvx\}++____________________________________________________________________________________________________________+
~++++++++++++++++++++++++++++++++++_{wCrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjxxdaOjrrrrrrrrrrcqwzunuux\-+______________________________________________________________________________________________________________+
~++++++++++++++++++++++++++++++++++~+vOUrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjjndoUrjrrrrrrrjrLqOunx|]_++_+__+_________________________________________________________________________________________________________+
~+++++++++++++++++++++++++++++++++++~|Z0xrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrrrrrrrrrrrCpqnrrrrrrrrrrvOaXj)]_+__________________________________________________________________+_+___________________________________________+
~+++++++++++++++++++++++++++++++++++~-0wurrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrjrrrrrrrrrjrnLkCnrrrrrrrrrjUhC|-++___________________________________________________________________+++___________________________________________+
~+++++++++++++++++++++++++++++++++++++zmJxjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrxxrrrrrrrrjfuqaJjrrrrrrrrfxYmt++_+________________________________________________________________+~1x)-__________________________________________+
~++++++++++++++++++++++++++++++++++++~fJmrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrrrrrrrjrxcvrrrjrrrrjjrLomnjrrjrrrrrrnpc{<_+________________________________________________________________+?zaz-+________________________________________++
~+++++++++++++++++++++++++++++++++++++)zpxjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrrrrrrrrrjvCmzjrrrrrrrrjzmdzjrrjrrrrrjxZQr~____________________________________________________________++__+~)vboU?~________________________________________+<
~+++++++++++++++++++++++++++++++++++++_jqujrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrrrrrrrrrjrrcpqXjrrrrrrjrxzk0njrrrrrrrjrzwU+_+_____________________________________________________________+~)0w0qL[<_______________________________________+-}
~+++++++++++++++++++++++++++++++++++++~\mcxrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrxuxrrrrrrrrrjrfrCkmrrjrrrrjrrxwwYrrrrrrrrrrnw0]_+__________________________________________________________+__~{zmLcZL}<-______________________________________+}r
~+++++++++++++++++++++++++++++++++++++~)CLvrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrXmYxjrrrrrrrrrrrxqhXrrrrrrrrrjzkqnrrrjrrrrrr0Zf++___________________________________________________________++/LwzjvQL1~______________________________________+_tw
~+++++++++++++++++++++++++++++++++++++~}cZzjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjXdwzjrrrrrrrrrrrrLpOxjrrrrrrrjxbkYrrrrrrrrrrzQv-+___________________________________________________________~]YqJrjvQZ)<______________________________________~}cb
~++++++++++++++++++++++++++++++++++++++?jqYjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjuLaCxrrrrrrrrrrrjuOkzrrrrrrrrrrZdOrrrrrrrrrruCU[+__________________________________________________________+?rqLurjv0m)<______________________________________<\Ym
~++++++++++++++++++++++++++++++++++++++_}dUrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrjrrrrrrrrrrrrrrrjnbmYjjrrrrrrrrrjjXhwcjrrrrrrrfXwhnjrrrrrrrrrUZ/?+__+___________________________________________________-+_]vZQnjrjnUO(<___________________________________++_~zOU
~+++++++++++++++++++++++++++++++++++++_~-wQujrrjrrrrrrrrrrrrrrrrrrrrrrrrrrjrxxrrjrrrrrrrrrrrrrjr0bOrjrrrrrrrrrrfuphUjrrrrrrrjnQ*zxjrrrrrrrjXmx]+__+____________________________________________________~+fOwujjrrxXO|~___________________________________+_+_Lwc
~+++++++++++++++++++++++++++++++++++++++_0OYjrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrnYYznrrrrrrrrrrrrrrrrXhbnrrrrrrrrrrrfx0*LrjrrrrrrrrUkQujjrrrrrrjc0x]+__+____________________________________________________~+QwQjrrrrxzw/~___________________________________-_+]0Zx
~++++++++++++++++++++++++++++++++++++++~_uZQjrrjrrrrrrrrrrrrrrrrrrrrrrrrrcmoWMWownrjrrrrjrrrrrrrrZkLjjrrrrrrrrrjrYdwujjrrrrrrjcwkXfrxrrrrrjvZQ)~__+_________________________________________________+_~-/dUjrrrrjrvwj-+_______________________________+___~~|wOf
~++++++++++++++++++++++++++++++++++++++++tOZjrrrrrrrrrrrrrrrrrrrrrrrrrrrxmoW888W#mcrrrrrjrrrrrrrrUwOxjrrrrrrrrrjrvZdzjrrrrrrrjnCkYjrrrrrrrjn0w|~__+________________________________________________-_-~(L0vjjrrrjruwx?+_______________________________+__++_xOUf
~++++++++++++++++++++++++++++++++++++++++)Owjrrrrrrrrrrrrrrrrrrrrrrrrjjrzo&&&&&&8oZcjjjrrrrrrrrrru0qurrrrrrrrrrrjnJbUrrrrrrrrrrchCxrrrrrrrjx0p|~__+__________________________________________________+-rbzrrrrrrrrnwu]+________________________________+~~+-YQvf
~++++++++++++++++++++++++++++++++++++++++[Cmrrrrrrrrrrrrrrrrrrrrrrrrrjju0&&W&&W&&%WwujjrrrrrrrrrrfJkLurrrrrrrrrrjrnd0urrrrrrrrrxomcjrrrrrjju0w|~__+__________________________________________________~jLwrjrrrrrrrxZz{+_______________________________+]}]-)0Crf
~++++++++++++++++++++++++++++++++++++++++-XOurjrrrrrrrrrrrrrrrrrrrrrrjjzbW&&&&&&&&&oXjrrrrrrrrrrjjzqwcjrjrrrrrrrrjxmwYrrrrrrrrjrkwYrrrrrrjju00(+-__________________________________________________+__UwUjjrrrrrrjrQY|+___________________________+____rcx)rmYff
~++++++++++++++++++++++++++++++++++++++++_cZcrrrrrrrrrrrrrrrrrrrrrrrrjjXkW&&&&&&&&&WQnrrrrrrrrrrrjnmaUjrrrrrrrrrrjrQb0rrrrrrrrrrkwUrrrrrrrjuOQ|+-__________________________________________________++{OqujrrrrrrrfrLCt++__________________________+_~?jmZOQZOvff
~+++++++++++++++++++++++++++++++++++++++++rLCrjrrrrrrrrrrrrrrrrrrrrrrjfY*&&&&&&&&&&8dJrrrrrrrrrrrrxChQrjjjrrrrrrrrrXdmxrrrrrrrfrkdCjjrrrrrfcZY1+-__________________________________________________+-cOYxrrrrrrrrjrJOu++___________________________+?rmJcXCJcrjf
~+++++++++++++++++++++++++++++++++++++++++fCLrjjrrrrrrrrrrrrrrrrrrrrrjfU*W&&&W&8&W#*aOrrrrrrrrrrrrrYbZnfjjrrrrrrrjjnppujrrrrrrjrkdCfrrrrrrjzmc[+-______________________________________________+__++[LLnrrrrrrrrrrjzZc____________________________+~)Ydxrrnnrrjf
~+++++++++++++++++++++++++++++++++++++++++tJQrjrrrrrrrrrrrrrrrrrrrrrrrfzkW&&&&WWWoqw*purjrrrrrrrrrrXbqvfrjrrrrrrrrrxdkcjjrrrrrjrkqUfrrrrrrjYmr?+-_________________________________________________+-/OUrrrrrrrrrrrjcOz-____________________________<fQmrrrrrrrjf
~++++++++++++++++++++++++++++++++++++++++~}cmxjjrrrrrrrrrrrrrrrrrrrrrrrzbWWW*kwUcxrrbkXrjrrrrrrrrrjv0bXfrrrrrrrrrjrjmdUjrrxrrrfrbwYjrrrrrrxUL}+___________________________________________________+)LOcjrrrrrrrrrrrxmL}++__________________________+JwYjjrrrrrjf
~++++++++++++++++++++++++++++++++++++++++~?xwxrrrrrrrrrrrrrrrrrrrrrrjrjvQqmOUXvxrrjrqkUjjrrrrrrrrrjnJdUjrrrrrrrrrjrjZdLjjrxrrrjrbwUjrrrrrjcQY-+___________________________________________________+twQxrrrrrrrrrrrrrwO(+_+________________________+?0wvrrjxxjrjf
~+++++++++++++++++++++++++++++++++++++++++-rmxjrrrrrrrrrrrrrrrrrrrrrrrjxvYzujjfjrrrjZdCjrrrrrrrrrrjxYbUjrjrrrrrrrjrrOdOrjrrrrrrrhwXjrrrrrrLOj+~________________________________________________+++-udJrjrrrrrrrrrrrjmOt~+_____________________-__++[Owxrrrrrrrjf
~+++++++++++++++++++++++++++++++++++++++++-jwujrrrrrrrrrrrrrrrrrrrrrrrjjjjfrrrrjrrrjOdOrjrrrrrrrrrjrckLxjrrrrrrrrjrrLqwjjrrrrjrno0urrrrrrcwC]++__________________________________________________<}LwzjrrrrrrrrrrrrjC0v++___________________++++_+_(ZZrjjrrrrrjf
~++++++++++++++++++++++++++++++++++++++++++fqcrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjQqmrjrrrrrrrrrjruqLnrrrrrrrrrjrrLqwjjrrrrjrzkJnrrrrrr0Oc_-+__________________________________________________>)OCujrjrrrrrrrrrjjUOQ-++__________________++-?-~+jZLjrjrrrrrjf
~+++++++++++++++++++++++++++++++++++++++++~/qzxrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrfQpmrjrrrrrrrrrrjxdOujrrrrrrrrjrjCqwrjrrrrfnCkUrrrjjrvhU)_+__________________________________________________+~\mYnjrrrrrrrrrrrjjcQw-+________________+-_?|cYti+uOCrrjrrrrrjf
~+++++++++++++++++++++++++++++++++++++++~+-xwcxrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrfCqdrrrrrrrrrrrrjxqOcjrrrrrrrrjrjOdOrjrrrrjzpqcfjjjcOkv{+____________________________________________________+-rwvrjrrrrrrrrrrrjjrJd{__________________~-xZ0pO1+v0Xxrrrrrrrjf
~+++++++++++++++++++++++++++++++++++++~_{frCqvrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjzmaxjrrrrrrrrrrjxmOzrjrrrrrrrjrjZb0rjrrrjjJopUnuvzQqw]~~____________________________________________________~}cmnrjrrrrrrrrrjrrjfYpt?+_______________+~10wULmYjLCvrrrrrrrrjf
~+++++++++++++++++++++++++++++++++++++~}cm0qbcrxrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrruZ*xjrrrrrrrrrrjuw0zjjrrrrrrrjrjZb0rrrrrjnL#kOCC0qmX)~_+____________________________________________________~(Umxjrrjrrrrrrrjrrjfcwc}<________________-jwYurXbpkYrjrrrrrrrjf
~+++++++++++++++++++++++++++++++++_++~fJJ_,}pJujrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjxCkzrjrjrrrrrrrrndOvrrrrrrrrrrrrpkXfjrrrjOZuxcULXu[+________________________________________________________+fCJrjjjrrrrrrrrrrrrjuJ0)~_+____________+_fLQnjrjuccjjrrrrrrrrjf
~+++++++++++++++++++++++++++++++++++~1JX[".>OwcjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrJkYxjrjrrrrrrrrnqOvrrrrrrrrrrrnppnrrrjrXqJ{][1)}[_++_-______________________________________________________u0Xrrjjrrrrrrrrrrrrrxzwt++______________[Ymcrrrrrxrjrrrrrrrrrjf
~+++++++++++++++++++++++++++++++++++?vU)"`.;chUrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjYdLvrrjrrrrrrrrupQujrrrrrrrrrrXbqvnxncJZJ/+~~<<~~+_-______________________________________________________+-cOzrrjjrrrrrrrrrrrrrrupv{+____________++|Owrrrrrrrrrrrrrrrrrrjf
~++++++++++++++++++++++++++++++++++[rC?`''''{dQrjrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrjcZqzjrrrrrrrrjxXaLfrrrrrxrrjrnOMoOLQQOOU[>~+__+___________________________________________________________+-XZcjrrrrrrrrrrrrrrrrjx00r<____________+~vm0jrjrrrrrrrrrrrrrrrjf
~++++++++++++++++++++++++++++++++++|Lx;.''`.~XZzjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrjvLkYjrrrrrrrrjnUoCrrjrrrrrrrrYb&*dOmmv/]~~~~+_+____+_______________________________________________________?CwujrrrrrrrrrrrrrrrrjrJOz~__-_________+_L0Xjrjrrrrrrrrrrrrrrrjf
~++++++++++++++++++++++++++++++++++j0(`'.''.I|qYjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjxzoQxjrrrrrrrjvZ*qXfjrrrrrrjzmkobC\))[-~<~~~~+~+__________________________________________________________+[LmrrrrrrrrrrrrrrrrrrjrvmQ?+_________-++}pLnjrrrrrrrrrrrrrrrrrjf
~+++++++++++++++++++++++++++++++++1Yji''''''.IY0zrjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrxaqUjrrrrrrrrUoqhhLrjfjrfrJhpCOpwUzu)+<<~~~<<~~+______+_+_______________________________________________++}LmrjrrrrrrrrrrrrrrrrrrxLZr+~+-_-__++~>)0Zcjrrrrrrrrrrrrrrrrrrjf
~++++++++++++++++++++++++++++++++-fY],''''''.`(wQjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrZkZrrjrjrjjuZaCmhdJzuuuzLwkLnCqmuczuf)+<~<<<<~~___-____________________________________________________++{Qwrjjrrrrrrrrrrrrrrrrrrz0U?++_+_++_-?)XdYxjrrrrrrrrrrrrrrrrrrjf
~++++++++++++++++++++++++++++++++)uj,''`'''''.:QkcxrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjuqkJnjfjrrxQhLvrXZhdwwwbhqcjjC0v`^>\XCt?<~~<~~~+_+_____________________________________________________++)0wrrjrrrrrrrrrrrrrrrrrjjYOx]~_-+])xnzmmCrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++++++++++++++++++++++_fc{^'''.'''.`'rpwXxrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjUqhJnrrrnQbdcxrrxCwkbbqUvjrjX00^'`^lxCj+~~~<<<~~~+____________________________________________________+_10wxrrrrrrrrrrrrrrrrrrrjjvZQ1~__]xLpdd0zrjrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++++++++++++++++++++++-XU<`.''''''''.+cMbQnjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrjnUbhqQQZdkpYrrjjjncYXXzxrjrjvOb:.''`izCt~<~~<~~~~~++__________________________________________________++)0wxrjrrrrrrrrrrrrrrrrrrjrLpr+~_cZwUYYvxjjrrrrrrrrrrrrrrrrrrrrjf
~++++++++++++++++++++++++++++++~1Cc`.''''''''.'`]dohpLujrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrzCZqqwOCcrjrrrrjrrrxrjrrrjYd*+^'''.+jQt?>~<~~~~~~~~_________________________________________________+_)0mrrjrrrrrrrrrrrrrrrrrrrjcOO{_\pQvxrrjjrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++++++++++++++++++++++tUt'''''''''''..iYbZmwOzxrjjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrjjrcJCYvrjrrjrrrrrrrrrrrrrvZak):.``.^+nJf[~~~~~~~<~~~+_______________________________________________++{QmrjjrrrrrrrrrrrrrrrrrrrjxXpx|YZvfrjrrrrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++++++++++++++++++++~+vv}.'`''''''''''^(wcrComUvrrrjrrjrrrrrrrrrrrrrrrrrrrrrrrrrrjjjjrrrrrrrrrrrrrjrrrrxxLddOj!''''.^iLJr-++~~~<<<~<~_-_-____________________________________________+}QmrrrrrrrrrrrrrrrrrrrrrrrjxZLLqcrjjrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~++++++++++++++++++++++++++++~-1Z),...'''''''''''irL\+}0ha0zurrrjrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrxrrrjrrrrruZoq|[uQ+''''.''I{zOzj]+~<~~~~~__+_--___________________________________________?Cwnrrrrrrrrrrrrrrrrrrrrrrrjxb#kxjjrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~++++++++++++++++++++++++++++<}vY~'..''''''''''''"~Cv{+(fYqqwLcrjjjrrrrrrrrrrrrrrxrrrrrrrrrrrrrrrrrrrrrrrrjjjrcOqpQj+_\Q-.'''''.';~)xUUx{<>~~~~++~+_-___________________________________________?X0urrrrrrrrrrrrrrrrrrrrrrrrrwamrjjrjrrrrrrrrrrrrrrrrrrrrrrrrrjf
~++++++++++++++++++++++++++++-f01:.'''''''''''''``^tLx~><1YLmm0LXcnrjjjjrrrrrrrrrrrrrrrrrrrrrrrjrrrrrrjrrxnvUL0mmz\->_10]'''''.'`..;-tUUx(]_<~~~<<++_-__________________________________________-zZvrrrrrrrrrrrrrrrrrrrrrrrrjmkCjjrrjrrrrrrrrrrrrrrrrrrrrrrrrrjf
~++++++++++++++++++++++++++++cCn`'''''''''''''''''',XL|<>><_1nJmqmOJYYcunrrrrrjjjjrrrjjjjrrrrrjjrrrrxuczY00OqwJf{i>><~?w)".''''''''''.l{nCzj}-+<<~~~+-_________________________________________++Uqzrrrrrrrrrrrrrrrrrrrrrrjrxpbzjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++++++++++++++++~+{QX<'''''''''''''''''`''}XQ+<<<<~+-}uCmpdbOLYcnxxrrrrrrrrrrrrrjjrrrxrxnvXCZwdoqJf}-+~><<<>+q/;.'''''''''.'``"(XCu\]~~~~~____________________________________________+vZUjrrrrrrrrrrrrrrrrrrrrrrrupwujrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~++++++++++++++++++++++++~_{zc{"'''''''''''''''''''.;/w\->>>>>>~?{|rvUOwpkqmZQQJUYXXXXXXXXYUUCLLmZwbkq0Jcx/1-~>><~<><>+qj!'''''''''''`''`;+)vQc]~>~<~~++_________________________________________tJLjrrrrrrrrrrrrrrrrrrrrrjrckpnjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++++++++++++++~~\CJ+`'.''''''''''''''''''..l\Of-><><<<>><+_?)|/nucYUOwmmmwwOmpwZZmmwZJCzXmqu{[_<<>><<<<<<<<>+Zx~'.''''''''''''''.^>1rJY)~<<~<~+_______________________________________~1zOxrjrrrrrrrrrrrrrrrrrrrrjcpOrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++++++++++++++~[zQ|,..''''''''''''''''''''.`lOU/>~<<<<<<<><>>i>+]})tnczczUXczJYzccczn/\}1zZ(i><<<<<<<<<<<<<>~Qn_..'''''''''''''''.."~cLu([~<~<~~+____________________________________-+[uwnrjrrrrrrrrrrrrrrrrrrrrruJYjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++++++++++++++_tL(I''''''''''''''''''''''.'.`rwJ<><<<<<<<<><<<<<<<~~+++~+++++++++++++~~<-vq\>>><<<<<<<<<<<<>+0u_'.'''''''''''''''''``l{JCn]<~~~~~+___________________________________-_-jmcxjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++++++++++++~?cC}`''''''''''''''''''''''''''',rZz+><<<~<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>~jq/><><<<<<<<<<<<~>~0Y{..'''''''''''''''''''''I)CQr-+~~<~+_-_+________________________________>)ZJujrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~++++++++++++++++++++~+cUf,`''''''''''''''''''''''''''''!jO/?<~<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>~rpf<<<<<<<<<<<<<<<>+Uz{'.'''''''''''''''''''''`I[mbJ1+<~<<____________________________________>{0Ocjrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~++++++++++++++++++++-|Lr~..''''''''''''''''''''''''''''.~LC|<><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<~fpx+<<<<<<<<<<<<<<>~Yz{'.'''''''''''''''''''''..^Uobn/{<~~+++________________________________+~?Ywzrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++++++++++?jO/!.''`''..'''''''''''''''''''''''''{mC[>~<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<~>\qv_><<<<<<<<<<<<>~1wU{..'''''''''''''''''''''.'.[YmuUX|}+~<~++______________________________+_+tqLxjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~++++++++++++++++_++tUC;`'''''.'''''''''''''''''''''''''''I|0f-<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>\qv-<><<<<<<<<<<<<{XoC1'.'''''''''''''''''''''''.I/m<?nOu{~~~~~++_____+________________________+(QOvjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~++++++++++++++++++1JX[`''''''.'''''''''''''''''''''''''''`lj0n<><<><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>1LY]><<<<<<<<<~<i/UZdL|'.'''''''''''''''''''''''.`?J)>>u0J{<<~~~++_____________________________+]nOYjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++++++++{Cr<`'''''''.'''''''''''''''''''''''''''`':cZU~><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>[v01i<><<<<<<<>-nmJ|JY('.'''''''''''''''''''''''`.I)Q?.:-rCc1~<<~______________________________++[C0vjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++++_++1uJ_'``''''''''''''''''''''''''''''''''''''.?cwt{-~>>><<<>~<<<<<<<<<<<<<<<<<<<<<<>]rO|i><>><~>i+|r0C/+Uz}'.''''''''''''''''''''''''.^<m),.^~vUv1+<+++++_-_________________________~-vmUrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++++_+-vZ/".''''''''''''''''''''''''''''''''''''.'''+zpCf?+~~<>><<<<<<<<<<<<<<<<<<<<<<<<<_|O/>><><>>~~10qU}>+QY{..'''''''''''''''''''''''`'.^Ln_'..I(CX1~<~<++___________________________~+|mZxrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++++++tL|I.'''''''''''''''''''''''''''''''''''''''.''Iw**q0X(?+~~<<<<<<<<<<<<<<<<<<<<<<<>>-Cc[<<<<-[tOqY|-<>+0X{'.'''''''''''''''''''''''`''`|Cx.'''`IzwY_+~~<~+___________________________+JwXrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++++~fYjl^'`'''''''''''''''''''''''''''''''''''''''''`}LhmJL0Jz\]<>i>><<<<<<<<<<<<<<<<<<<>+YY)>>_|UQOYr{_~<>+0v?..''''''''''''''''''''''''''`<JY^'''.'~tYYt-<~<~++_______________________+-<u00rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++++]YY+`'''''''''''''''''''''''''''''''''''''''''''..,)YQcvC0QUnt|)}-+~>>>>>><<>>>>>>>>>>~uLv|txYOLU|->>><>~0u_..'''''''''''''''''''''''''..;vJi`'''.'!(CUj_~<~~+-__+_____________________~\Uqxjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++_+_{cu?.''''''''''''''''''''''''''''''''''''''''''''.'''>YLj_[|cCOO0Czuf\(1}[[[[[[[[[[{1(|tYpd0ZQX(_>>>><<<>~Qr+..'''''''''''''''''''''''''''^{z\`.''''.'<rCx{+<+~_+_______________________+-fqzrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~++++++++++~}cL[".''''''''''''''''''''''''''''''''''''''''''''`'''`{Zq|<~+?1tuUwppqZUcnuuunuuuuuXLZpppwCu|]+~<<<~<<~<>+0f>'.'''''''''''''''''''''''''''`>rX,..''`''',}QY}+~~~~+_______________________~(0Lujrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++++jZnl''''''''''''''''''''''''''''''''''''''''''''''''''.I[JL\>>~~-[1|txvYXzUQ0LJ00000XYYujt(1[_~>><<<<<<<<>+wtI''''''''''''''''''''''''''''''^)Ji`.''''''':/UC1+<~<~++____++______________-~1UZcjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~++++++++~~)Cf<''''''''''''''''''''''''''''''''''''''''''''''''''..''iUOc<i><><>>+-][[{)()1)))))[}]+~<<<<>><<<<<<<<<<~?q/;''''''''''''''''''''''''''''.'.+U\l.'''''''':~/0v)<<<~+___________________++~_|wYrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~+++++++++}uX<^.''''''''''''''''''''''''''''''''''''''''''''''''''`...{UO/-<><<<~<>>>>>>i>>>>>>>>>><<~<<>><<<<<<<<<<<~[w|,'''''''''''''''''''''''''''''''icz~.''''''''.'lzJv[~<<~+++________________+-]]{bCxrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~++++~++~1YY~`'.''.'''''''''''''''''''''''''''''''''''''''''''''''''`..;\ZY|~><><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>+}m}`''''''''''''''''''''''''''''.''^/w{'''''''''''.^?nU\]~~<<~++___________-+?1rvucMOujjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~++++++++vY/.`.'''''''''''''''''''''''''''''''''''''''''''''''''''''''.`"rOQ}+<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>-(Q?`''''''''''''''''''''''''''''''''}Z/^'.''''''''..'>YOt_~~~<+++___________+1zLYYQ*mzrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjf
~++++++_}Qf<",^.'.'''''''''''''''''''''''''''''''''''''''''''''''''''''''>\UJ\-><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>]rQ-'''''''''''''''''''''''''''''''`.-CxI.''''''''`'.'^[vCt?<<<~~~+_________+-fL\+<?OmJfjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjjf
~+++++~|whLccvzx)i`.''''''''''''''''''''''''''''''''''''''''''''''''.''''.:~cmC]i<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>[nU~'''''''''''''''''''''''''''''...'lfY+..'''''''''`..'!)CY-<<~<~++++______<}Xj>"IinOQjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjuC
~++_+~{vkQYcvcYXvf}~^.`''''''''''''''''''''''''''''''''''''''''''''''''''''`?zOu)+><~<>>>>>i><<<<<<<<<<<<<<<<<<<<<<<>}zc>.'''''''''''''''''''''''''''''''.:[C?''''''''''''''.`;rJj}_<~~<~+_____++~|C}:I-fYOQrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrcCO
~+++_~uQz[>lI!>}jOOX>''''''''''''''''''''''''''''''''''''''''''''''''''''''`^I/wL{+<>><~~++_~<<><<<<<<<<<<<<<<<<<<<<>)Qr!.''''''''''''''''''''''''''''''''^iY)^''''''''''''`''`l|Zc}~<~~~+_+_____+fU>`^{ZddQjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjuwmY
~++++fLr,`''''``^I[vOn>^'''''''''''''''''''''''''''''''''''''''''''''''''''`''`?cdc}~_}uCmqQr_><<<<<<<<<<<<<<<<<<<<<i)O):.`''''''''''''''''''''''''''''''''^xn-`'''''''''''''''``}CY{+<~<~~~+__+~1vx,..^_h*ZjjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjvCbJ|-
~+++-Ur~^.'''''''`:irJX>^.'''''''''''''''''''''''''''''''''''''''''''''''''.''',~uZUuUwqmOZw0{><<<<<<<<<<<<<<<<<<<<<>\m-,'`'''''''''''''''''''''''''''''''.^|X(`''''''''''''''''';?uUf~~~~~~~++++/c|`.'.,tmbXrjjxjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrxrrrrjruOqC(-+
~+~]jL?`.`'''''''''.<rQj_".''''''''''''''''''''''''''''''''''''''''''''''''`''.'`)wkwpkmCzYOp|i<<<<<<<<<<<<<<<<<<<<<<tw>^.'''''''''''''''''''''''''''''''''`]Uj^'''''''''''''''''.`?LJ|~<<~~~~+-_nY]'.''.;t0wUxrrrjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrzQwC/+~+
~~_nmt,.'`'''''''``'.,-CU|^''''''''''''''''''''''''''''''''''''''''''''''''''.^>)C0qQzrjjjuLw(>><<<<<<<<<<<<<<<<<<><[uZ:'.''''''''''''''''''''''''''''''''.'!Uc,'''''''''''''''''...]nL(_<<~~<~_?YXl`.''''`+LpZzxjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrjrn0m0t-~+++
~~}Xc~..'`''''''''''..`[JLi''''''''''''''''''''''''''''''''''''''''''''''''``^<zqkJvrxrrrrXZU]><<<<<<<<<<<<<<<<<<~><\UQ"'.`''''''''''''''''''''''''''''''''':YU!''''''''''''''''''.`'>jJ\_~~~~~~?Uz,`.'''.''+zkmzjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrruCaJ|+____+
~?jY?".''''''''''''''..;(Yrl`.'''''''''''''''''''''''''''''''''''''''''''...i|Jm0YujjrrrrrJkc->~<<<<<<<<<<<<<<<<<<<>/YU`.'''''''''''''''''''''''''''''''''''`cU+`.'''''''''''''''''''^<zLn<~~~~~)Cu''''''`.."<\OpLurjrrjrrrrrrrrrrrrrrrrrrrrrrrrrrrjCqwc)?~____+
_uC}`''''''''''''''''''."]Jv>'`''''''''''''''''''''''''''''''''''''''''..'!)LpOznrrrrrrrjnmWw1<><<<<<<<<<<<<<<<<<<<>uUt`''.'''''''''''''''''''''''''''''''''.\Xr`.'''''''''''''''''''.`>/Yu+<~>~xz|..''''''''."_jqhmcrjjrrjjrrrrrrrrrrrrrrrrrrrjjrvQmYf_++__+__+
/Cc:`'`'''''''''''''''''':x0|"''''''''''''''''''''''''''''''''''''''''..'~jLqOcfjxjrrrrjjzqZOc/[>><<<<<<<<<<<<<<<<<>UL}`.'.'''''''''''''''''''''''''''''''.`.}vU^..''''''''''''''''''''`!\Cf]~<+Yx?..''''''.''``iuOm0CcxrjjjjrrrrrrrrrrrrrrrrrrjnUmdz(_~+_____++
0z}..'''''''''''''''''''''-CX>''`.'''''''''''''''''''''''''''''''''''''`IXdkzxrrrrrrrjrjrLm1\0Zn+~<><<<<<<<<<<<<<<<>JC+`'''''''''''''''''''''''''''''''''''''+nL^.'''''''''''''''''''''.'Iumj+>+Cf>'`'''''''''''':+fbhmznrrrrrrrjrrrrrrrrrrrrrrrzbod(~+________+
L-'..'''''''''''''''''''`.`>Qfl'''''''''''''''''''''''''''''''''''''''l(OpYxjjrrrrrrrrrxUZx"`l)Cqn}~<<<<<<<<<<<<<>~[0YI'''''''''''''''''''''''''''''''''''''',(mI'''''''''''''''''''''''`'l(Lt+_L(I.'''''''''''''''^i1XwpqCzurrjrrrjjrrjrrrjrrcmpv1zt?+_+______+
};''''''''''''''''''''''`.."fU)^.`''''''''''''''''''''''''''''''''''':uqwXnrrrrrrrrrrrrxqm+`.^;?J0J(>><<<<<<<<<<<>~(0v,'''''''''''''''''''''''''''''''''''''''}mi`.''''''''''''''''''''''``I|Cv1L[`''''''''''''''''.`:~{jUqww0JvrjffjjrrxjjjxUdmxiI/v|-_+______+
"`.'''''''''''''''''''''''.'~LY!'`''''''''''''''''''''''''''''''''.^l)pdJrjrrrrrrrrrrrrXdC"'`'.`}uLY/]<<<<<<<<<<<>~jLf^'``''''''''''''''''''''''''''''''''''''?0[:.''''''''''''''''''.''''.'!c0YL_.`''''''''''''.''''''^>}uY0mZQJUXcvnxrjjrrUZZr~.'-Uc?-+______+
..'''''''''''''''''''''''''..jQr`.''''''''''''''''''''''''''''''..^[zdLxjrrrrrrrrrrrrjnpU[.`'''`''+XOU\}+>><<<<<<<~zv?`''''''''''''''''''''''''''''''''''''''.>vni.'''.'''''''''''''''''''''.ljhui.'''''''''''''''''''''..',>)fzLOZOZ0CUUYUmkc?`.'`^zQ(+-______+
'''''''''''''''''''''''''''''_xC:`''''''''''''''''''''''''''''''.'>CoOrrrrrrrrrrrrrrrrvotl'''''`'.'!(Cmz{~<<<<<<<>+zt>'''''''''''''''''''''''''''''''''''''''.ijc<.'''''''''''''''''''''''''.'?0(I.'''''''''''''''''''``'''''^^"+}/cQmqpddaMm1<".'..tXj++______+
''''''''''''''''''''''''''''',)m?:.''.''''''''''''''''''''''''''`~xpLvjjjjrrrrrrrrrrrvL0?'````''.'.`l_XOC\->><<<<+1L1,.''''''''''''''''''''''''''''''''''''''.I1C_..''''''''''''''''''''.''''.]m};.''''''''''''''''''''''''''..'^:I>+?)/jvU0OXu>`.'')zv+~______+
'''''''''''''''''''''''''''...>xz~.''''''''''''''''''''''''''`.'}LpUrjrrrrrrrrrrrrrrrJa1;''''''''''.'.l[rZCr-><<<?j0?..'''''''''''''''''''''''''''''''''''''''"~Z}''''''''''''''''''''''''''.,(mI`.'''''''''''''''''''''''''''''......`",Ili~-+:'''._jU+~______+
''''''''''''''''''''''''''''..,?O[`'.'''''''''''''''''''''''''`lJdmjjjrrrrrrrrrrrrrjcZdi`''''''''''.`..^>cLCj}+<>{zJ~..''''''''''''''''''''''''''''''''''''''''Iw(^.''''''''''''''''''''''''.ifZ"'''''''''''''''''''''''''''''''''''''..''....'.`'''itL+~______+
'''''''''''''''''''''''''''..'';Z/I.'''''''''''''''''''''''''`I|aOnjrrjrrrrrrrrrrrrjLZX^'''''''''''..'''':}YZX1~>(QnI.`'''''''''''''''''''''''''''''''''''''''',mt;'..''''''''''''''''''''''._nL^.'''''''''''''''''''''''''''''''.......''''''''.'''>tC_+______+
'''''''''''''''''''''''''''''''^fY/.`''''''''''''''''''''''`.IfhYnjrrrrrrrrrrrrrrjrrdO~`''''''''''''''''''',(Ldu}rq(^'`.'''''''''''''''''''''''''''''''''''''''^Lu_..'''''''''''''''''''''''.\Ur^..''''''''''''''''''''''''''''''''''''''''''''''''.}vz++______+
'''''''''''''''''''''''''''''''`[Jc`''''''''''''''''''''''''.fZqnjjrrrrrrrrrrrrrrjrcqz:'''''''''''''''''''.`;_fLOmZ-.'`''''''''''''''''''''''''''''''''''''''''^Uc[..'''''''''''''''''''''''.rU1`'.''''''''''''''''''''''''''''''''''''''''''''''''.|Uz+~______+
''''''''''''''''''''''''''''''''iYJ;'''''''''''''''''''''''`!LbUrrrrrrrrrrrrrrrrrjrLQ\^`''''''''''''''''''''.`ljLpp)^..'''''''''''''''''''''''''''''''''''''''.`xY|..''''''''''''''''''''''''cU_`.'''''''''''''''''''''''''''''''''''''''''''''''''.fCn+~______+
''''''''''''''''''''''''''''''''^fJ[^.''''''''''''''''''''`;uqCjrrrrrrrrrrrrrrrrrjnpx>'''''''''''''''''''''''''.;jLC\~:'''.'''''''''''''''''''''''''''''''''''.'{Cn..''''''''''''''''''''''',UYI`.`''''''''''''''''''''''''''''''''''''''''''''''''"cU{_+______+
'''''''''''''''''''''''''''''''`^{c\^.'''''''''''''.''''`',}ZLxrrrrrrrrrrrrrrrrrrrzh(^''.'''''''''''''''''''''.'`">nwY}^'''''''''''''''''''''''''''''''''''''.'']Jn.''.'''''''''''''''''''.`>Ju"''''''''''''''''''''''''''''''''''''''''''''''''''.>Yz?________+
'''''''''''''''''''''''''''''''''!/c:''''''''''''''.'''''.~UqzfjrrrrrrrrrrrrrrrrjnCp].''''''''''''''''''''''''''.'^itYLx+".''.'''''''''''''''''''''''''''''''''.iUY^''''''''''''''''''''''.`[Jf^'''''''''''''''''''''''''''''''''''''''''''''''''.`1Jx+_-______+
'''''''''''''''''''''''''''''''''`[Y_^'''''''''''''.''''.,jpCrrjrrrrrrrrrrrrrrrrjcOL>'.''''''''''''''''''''''''''.'.,>}YCz],..'''''''''''''''''''''''''''''''''':YC:'.''''''''''''''''''''.`~{+'''.'''''''''''''''''''''''''''''''''''''''''''''..,xu1+________+
'''''''''''''''''''''''''''''''''.+Y|;..'''''''''''.''''.iJwXrrrrrrrrrrrrrrrrrrrjYwcl.''''''''''''''''''''''''''''''.'`{uCc1i`....''.''''''''''''''''''''''''''',cC!'..''''''''''''''''''''',I,''''''''''''''''''''''''''''''''''''''''''''''''''`>zf-+________+
'''''''''''''''''''''''''''''''''.!uU~.''''''''''''.'''.,(dUnrrrrrrrrrrrrrrrrrrrjUbj,.''`''''''''''''''''''''''''..'''..`iuCz(~:''''.''''''''''''''''''''''''''.^rC]`..''''''''''''''''''''''.'''''''''''''''''''''''''''''''''''''''''''''''''''itU)<+________+
'''''''''''''''''''''''''''''''''':tL?.''''''''''''.''''_vmnrjjrrrrrrrrrrrrrrrrrjCof^'''''''''''''''''''''''''''''.'''.''`I]vmU]^`.''''''''''''''''''''''''''''.^/U{`..'''''''''''''''''''''.'.''''''''''''''''''''''''''''''''''''''''''''''''''~Xc[~+________+
'''''''''''''''''''''''''''''''`'.^(Z{'''''''''''''.'''^/QLrrjjrrrrrrrrrrrrrrrrrjLk|"'''''''''''''''''''''''''''''''''`.'.`,~fULx-,..''''''''''''''''''''''''''.^)z\^..''''''''''''''''''''''.'''''''''''''''''''''''''''''''''''''''''''''''''''}0x-+_+_______+
''''''''''''''''''''''''''''''''''.]O/"'.''''''''''''..!CdurrrrrrrrrrrrrrrrrrrrrrCq|`'''.''''''''''''''''''''''''''''''''''..,>{YCz],`.'`''''''''''''''''''''''.'?ur"'.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.IuO|++_________+
'''''''''''''''''''''''''''''''''''+YxI.''''''''''''`.'1mprrrrrrrrrrrrrrrrrrrrrrrJq/"''''''''''''''''''''''''''''''''''''''''''^{vLc)<"'.'''''''''''''''''''''''`<jn"..''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.>UY{+__________+
''''''''''''''''''''''''''''''''''.!rY<.''''''''''''`.^YZLjrrrrrrrrrrrrrrrrrrrrrrUpf,''''''''''''''''''''''''''''''''''''''`''..^l{CZX>^`'.'''''''''''''''''''''';|u,..''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''._C\-~__________+
''''''''''''''''''''''''''''''''''.I)C_.''''''''''''''ImQvjrrrrrrrrrrrrrrrrrrrrrrCp/^.''''''''''''''''''''''''''''''''''''''''''''':-vmU("`'''.'''''''''''''''''`,)YI'.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''^{L}++__________+
''''''''''''''''''''''''''''''''''.,-Y?..'''''''''''.,[dJrrrrrrrrrrrrrrrrrrrrrrrrJpf".'''''''''''''''''''''''''''''''''''''''''''''',i|z0x];.'.''''''''''''''''''`1Ul`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''>fX-~++_________+
''''''''''''''''''''''''''''''''''.^iX}`.''''''''''..lfqYjrrrrrrrrrrrrrrrrrrrrrrrUpr,.''''''''''''''''''''''''''''''''''''''''''''`''.:}cCc|>^.''''''''''''''''''.[U<".''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''?vu+~___________+
'''''''''''''''''''''''''''''''''''':z\;'''''''''''''+C0cjrrrrrrrrrrrrrrrrrrrrrjrUdr:..''''''''''''''''''''''''''''''''''''''''''''''`..'-rCY\?;'.'''''''''''''''.-J}:.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''`.|X\~+___________+
'''''''''''''''''''''''''''''''''''."xf>`''''''''''''[wYnrrrrrrrrrrrrrrrrrrrrrrrrUpr:..'''''''''''''''''''''''''''''''''''''''''''''''''.`"_zZQ];`.''''''''''''''.-C)I.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.nU[++_+_________+
''''''''''''''''''''''''''''''''''''^tu?`''''''''''',(pvrrrrrrrrrrrrrrrrrrrrrrrrrJp/"'''''''''''''''''''''''''''''''''''''''''''''.''.''..'^+)cCu+`.'.'''''''''''.~Jtl.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''^XL_+__+_________+
'''''''''''''''''''''''''''''''''''.`)Y|`''''''''''.-zdrrrrrrrrrrrrrrrrrrrrrrrrrrUp/"'''''''''''''''''''''''''''''''''''''''''''''..''.'''.'.`l1uJ\i'''''''''''''.<Yji.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.`>CU+___-_________+
'''''''''''''''''''''''''''''''''''.^}X/^'''''''''''1LprrrrrrrrrrrrrrrrrrrrrrrrrrJq|^'''''''''''''''''''''''''''''''''''''''''''''''''''''''..."_UL}`'''''''''''..<Yxi.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.`?Uc~-____________+
'''''''''''''''''''''''''''''''''''.`-zt^''''''''''./0ZrjjrrrrrrrrrrrrrrrrrrrrrrxCw)`''''''''''''''''''''''''''''''''''''''''''''''''''''''''''``}Oj:.'''''''''''.izz~'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''^1ct~-_+__________+
''''''''''''''''''''''''''''''''''..`iUu,'''''''''''zqUrrrrrrrrrrrrrrrrrrrrrrrrjxLw}''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.!jX>''''''''''''.InL-'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"xu}<~~+__________+
'''''''''''''''''''''''''''''''''''''ICz:'''''''''`^YwcrrrrrrrrrrrrrrrrrrrrrrrrrnQw]`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.;1J_''''''''''''.;xw?.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.'Ivt+~<<~~++______++
''''''''''''''''''''''''''''''''''''':JYl'''''''.'`;Jwurrrrrrrrrrrrrrrrrrrrrrrrjn0m?'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.."_U]'''''''''''''"tw[.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''."<z|>~~~~~~~+______+
''''''''''''''''''''''''''''''''''''''YJi'''''''..^<0wnjrrrrrrrrrrrrrrrrrrrrrrrfvOU~.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.'lU)"''''''''''''`(w{..'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''';1X)<~~~~<<~~+____++
'''''''''''''''''''''''''''''''''''.''XC~'.'''''.'^-ZmrjjrrrrrrrrrrrrrrrrrrrrrrjzOx!.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.,X/I'''''''''''.^(w1'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.ijc}<~~<<<~~~~+____+
''''''''''''''''''''''''''''''''''''.'vU-'''''''''^1Z0xjrrrrrrrrrrrrrrrrrrrrrrrjXO\!.''''''''''''''''''''''''''''''''''''''''''''''''.'''.'''``'..,ct!''''''''''''`}0)^.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.~Yv]<<<<~~~~~~+_+__+
''''''''''''''''''''''''''''''''''''''nJ{`''''''''^rZUrjrrrrrrrrrrrrrrrrrrrrrrrxCC~^''''''''''''''''''''''''''''''''''''''''''''''''''..',"`..`'.."ufi`'''''''''''']L/,..'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''?Qf+<<~~<~<~~~~~~+_+
''''''''''''''''''''''''''''''''''''''xU)`''''''.'"uOzrjrrrrrrrrrrrrrrrrrrrrrrrz0v:''''''''''''''''''''''''''''''''''''''''''''''''''.,i-(1?!`'...^rj<`'''''''''''.-Lf:..''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''`{Q\<<~<~<~~~<~<<<~++
'''''''''''''''''''''''''''''''''''''./z('.`'''''':zLurrrrrrrrrrrrrrrrrrrrrrjrjLm/;.''```'''''''''''''''''''''''''''''''''''''''''`''.-jCm0Ctl`.`'^/r?`''.'''''''..-Lf:.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''..;tL(<~~~~~~~~~~~~~~~~
'''''''''''''''''''''''''''''''''''''.\Uj`.''''''`iUJxrrrrrrrrrrrrrrrrrrrrrrrjnkOI`'.`''`'''''''''''''''''''''''''''''''''''''''''''^{0U[;i1LO}``'^/c{`''.''''''..._LuI.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''..ivv{<~~~~~~~~~~~~~<~~
'''''''''''''''''''''''''''''''''''''.\Uj^.'''''.^<JJrrrrrrrrrrrrrrrrrrrrrrrxzmhz:"'.'.''''''''''''''''''''''''''''''''''''''''''''`icv[;'^:|LxI''^/z{`''.''''''...+Uci.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''..~Jf]<~~~~~~~~~~~~~~~<
'''''''''''''''''''''''''''''''''''''.\Uj^.`''''.,-LUjrrrrrrrrrrrrrrrrrrrrrruQahL|)?>:`'''''''''''''''''''''''''''''''''''''''''''':}J{^'''.ijJ~.'^\c{`''.''''''''.<vvi.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''..-C)-<~~~~~~~~~~~~~~~~
'''''''''''''''''''''''''''''''''''''.|zj`''.'''.l/OXjjrrrrrrrrrrrrrrrrrrrrruLOZqbqmLv{I`.'''''''''''''''''''''''''''''''''''''''''>nci..'''^+C{^.^|c1`''.'''''''`.ijv>.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',)Y-<~~~~~~~~~~~~~~~~~
'''''''''''''''''''''''''''''''''''''.{ur^''````'ir0zjrrrrrrrrrrrrrrrrrrrrrxrrrrxuvYqdw|!`'''''''''''''''''''''''''''''''''''''''''<crl.'''''IY(".`1u1`''.'''''''`.!jU~.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''``>tz+<~~~~~~~~~~~~~~<~~
'''''''''''''''''''''''''''''''''''''.{vv`.'.'::^>cOcjrrrrrrrrrrrrrrrrrrrrrrrrjjjrxnzJZwr+.''''''''''''''''''''''''''''''''''''''''<zu!.''''`;U(".^1z|`''.''''''''.l\C_.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''^1zx+~~~~~~~~~~~~~~~<~<
'''''''''''''''''''''''''''''''''''''.}zz^'I\nUYxumOujjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrnOpU:`''''''''''''''''''''''''''''''''''''''.ifU~.'''',]C['.`1Y/`'..'''''''.."-L?.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.',rU}<<~~~~~~~~~~~~~~~~~
''''''''''''''''''''''''''''''''''''''}cz!+/YYYczZk0xjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrnww{"''''.'..'.''''''''''''''''''''''''''''."-U\I'..`+nY>..`1Y/`'..''''''''.^>C[.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.lcY<~<~~~~~~~~~~~~~~~~~
''''''''''''''''''''''''''''''''''''..1UmvUY{>,'iC#0xjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrxrrn0m];`.'''''''.'''''''''''''''''''''''''''..^)Lv?i>[zC1^.'^{Y/`'..''''''.'''lU)"'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.'|Uu><<~~~~~~~~~~~~~~~~~
'''''''''''''''''''''''''''''''.'''.`'/maL\<^`.."joLrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjYpz1I;:;;::"^`''''''''''...'''''''''''''''''"x0QruCC(l''.`{Y\^'.''''''''''.:U\;''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''..`cXf>~~~~~~~~~~~~~~~~~~~
'''''''''''''''''''''''''''.'''''.'">\LLx-l^....>CdYrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjnQpwJXXXXXzxj<^''''''''''''''''''''''''''''''i1xucx[I`''.`{U/^'.''''''''''."vt!`.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',Cr[<~~~~~~~~~~~~~~~~~~~
'''''''''''''''''''''''''''''..'.;?XQX)~:''.''.;tkzrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrrxXJCJCCCCL0mwc_`'''''''''''''''''''''''''''''`IiiI''.''.`?z/^'.''''''''''.^fn?''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.:]O|><<~~~~~~~~~~~~~~~~~~
''''''''''''''''''''''''''''.'`I?\uCX),`'''.`'.~cdrjrrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjfjrnnnnnuXCddv"'''''''''''''''''''''''''''''''..'.''''.`?zt^'.''''''''''.^)X(`'.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.ijU1<<~~~~~~~~~~~~~~~~~~~
'''''''''''''''''...''''''.``"i|ZqY?I^`.''''`.'}YQrjrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrrrrrrrrzmki`''''''''''''''''''''''''''''''...'''''.`}Y/^`'.'''''''''.`-Jr^.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.-C/?<<~~~~~~~~~~~~~~~~~~~
''''''''''''''''''''''''``;~(LZQ(i^^`.`''''''..|QQrrrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrrjrrjYp|l`````^"^^'``''''''''''''''''''''''''''.`-zt^''''''''''''.';JX:'.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.l\m-<~<~~~~~~~~~~~~~~~~~~~
''''''''''''''''''.'.''I-|cJUr)-I^...`'.'''''.'1JLrrrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrrrrrrrrfXwY}><-[|tr\[:'.''''''''''''''''''''''''''.`-Jr"'.''''''''''..^zY+'.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''-xU~<~<~<~~~~~~~~~~~~~~~~~
'''''''''''''.'..''^i+_|nYJXr~,'.'''''''''''''.{YQrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjuLmzfxvXCOZLU1l'''''..''.'.'''''''''''''''.'~Jn"'..'''''''''''.fX('.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''`tXf+<~<~<~~~~~~~~~~~~~~~~~
''''''''''''`":i~]1\cUUYr1i^..''''''''''''''''.}Y0xjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrLZwmwQLJzUqpnI''''...'.'..'.'''''''''''..'iUn"'..'''''''''''.-xC^.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''lYX-~~<~~~~~~~~~~~~~~~~~~~~
''''''''''''"<}nUQZ0u\?;"^'''.'''''''''''''''.'[UZrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrnunxxrxrrxwQ]''''```^``'`.''''''''''''..'iUu"'..''''''''''.'ltZI.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''^}zf+<<<~~<~~~~~~~~~~~~~~~~~
''''''''''..irYYnt)[>l,'''.''.'''''''''''''''..?Xmxjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjrrrrrrrjrjjmm/`.`l+[|\\\(_`.'''''''''''..'lCc"'..''''''''''''`[Z1;''''''''''''''''''''''''''''''''''''''''''''''''''''''''',nr}+~<<~~<~~~~~~~~~~~~~~~~~
''''''''''.',~_>l"`'...''''''''''''''''''''''''<xwxrrrjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjCwZncYLOOmZ0Omwc-,''..........':Jz^''.''''''''''.'';)0-''`''''''''''''''''''''''''''''''''''''''''''''''''''''.;)L\<~~~~~~~~~~~~~~~~~~~~~~~~
''''''''''''..'....''''''''''''''''''''''''''''!fwxjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjfcCwZmwmZ0CJUUQqwu+,,:l!i>~_--][1mCi'''''''''''''''''l0\l'''''''''''''''''''''''''''''''''''''''''''''''''''''''~cY}<~~~~~~~~~~~~~~~~~~~~~~~~
.'''''''''''''.'''''`'''''''''''''''''''''''''';\mrfffffffffffffffffffffffffffffffffffffffffffffffffffffffttttttttftfxYUzuxjjfffffxLmt<<-1tjxzC0Opqp#q(^..'''''''''''...^Xc[.'''''''''''''''''''''''''''''''''''''''''''''''''''''`[Lf+<~~~~~~~~~~~~~~~~~~~~~~~~

```


Running API tests
------------------------------------------------

1. Follow steps for running the test server above.
2. run `$ nosetests tests/`

Future Improvements
------------------------------------------------

* Expose image dithering output options.
* Settable ascii art output size.
* HTML output i.e <br> instead of newlines etc.
