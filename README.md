# where_to_go


### How to install ###

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```python
pip install -r requirements.txt
```

### How to use ###

Create static files from assets:

```python
python manage.py collectstatic
```

Create bd and apply migrations:

```python
python manage.py migrate
```

Start django:

```python
python manage.py runserver
```

Access site:
[Site](127.0.0.1:8000)

### Project Goals ###
The code is written for educational purposes on online-course for web-developers [dvmn.org](dvmn.org).
