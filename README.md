# URL Sharpner

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/gr8temi/urlshortner.git
$ cd urlshortner
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv myvenv
$ source myvenv/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Endpoints

```
1. To create a new shortened URL: 
    POST 'http://127.0.0.1:8000/'
    request body = {
        "original_url: "www.example.com
    }
    returns 
    {
        "short_url": host/short_code
    }
    NB: the generated URL can be tested on the browser and it should redirect successfully to the original URL. kindly make sure the server is up and running
```

```
2. To retrieve original URL: 
    GET 'http://127.0.0.1:8000/retrieve/'
    request param = ?url="{short_url}"
    returns 
    {
        "original_url": host/short_code
    }
```
```
3. To redirect to original URL: 
    GET 'short_url'
    returns a redirects to the original URL

```