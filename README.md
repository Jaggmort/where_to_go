# where_to_go? #

It's interactive Moscow map.
U can check how its look in the web [site](http://jaggmort.pythonanywhere.com/)\
U can get access to admin/manager forms by this [link](http://jaggmort.pythonanywhere.com/admin/)

## How to install ##

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```python
pip install -r requirements.txt
```

## How to use ##

### Create enviroment file ###

Create .env in main directory

`SECRET_KEY` - Secret Key. Example: `'django-insecure-wi&(nc+cup=@9$m=u1yud^a6$56fjd+1^^yt1j-0d&!@^-43mo'`\
`DEBUG` - `False`. If u need debug information set to `True`\
`ALLOWED_HOSTS` - List of allowed hosts, set to `'127.0.0.1'` for local use.\
`CSRF_COOKIE_SECURE` - `True`\
`SESSION_COOKIE_SECURE` - `True`\
`CSRF_TRUSTED_ORIGINS` - Set to web-address of your web-application.\
`SECURE_HSTS_INCLUDE_SUBDOMAINS` - `True`\
`SECURE_SSL_REDIRECT` - `True`\

### Create static files from assets ###

```python
python manage.py collectstatic
```

### Create bd and apply migrations ###

```python
python manage.py migrate
```

### Add location to map ###

```python
python manage.py load_place "json_url"
```

where `json_url` - path to url file with format:

{\
    "title": "place_name",\
    "imgs": [\
            "link_to_first_image", \
            "link_to_seond_image", \
            ...\
        ],\
    "description_short": "short description",\
    "description_long": "full description, html-tags included",\
    "coordinates": {\
        "lng": "longitude",\
        "lat": "latitude"\
    }\
}\

### Start server ###

```python
python manage.py runserver
```

### Access to site ###
[Site](127.0.0.1:8000)

### Project Goals ###
The code is written for educational purposes on online-course for web-developers [dvmn.org](dvmn.org).
