# django-websocket-request-example

## Overview
This example application uses:

- [django-websocket-request](https://github.com/GetBlimp/django-websocket-request)
- [Django](https://www.djangoproject.com)
- [Django REST framework](http://django-rest-framework.org)
- [SockJS](http://sockjs.org)
- [Tornado](https://github.com/mrjoes/sockjs-tornado/)

## Live demo

This example application is running on Heroku.

[http://dwr-example.herokuapp.com/](http://dwr-example.herokuapp.com/)

Note that Django is not running at all. Tornado is serving a static HTML file and is routing the websocket requests. django-websocket-request then does the magic.

Throttling is enabled and snippets are erased periodically. If you run into any errors feel free to bother [@jpadilla_](https://twitter.com/jpadilla_) on Twitter about it.

## Running locally

``` bash
$ pip install -r requirements.txt
$ python manage.py syncdb
$ python ws.py
$ open http://127.0.0.1:8080
```
