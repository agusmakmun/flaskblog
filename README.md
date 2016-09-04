The _Simple Flask Blog_ Official Code Base
-----

> **Simple Flask Blog** is a simple blog bassed on Python + Flask. This project maded for **[ProblemSet Competition from CodePolitan](https://www.codepolitan.com/problemset-python-dasar)**.


SCREENSHOT
-----

More screenshot you also can checkout at directory of `/screenshot`.

![Screenshot Simple Flask Blog](screenshot/screenshot.png)


TECHNOLOGY STACK
-----

* Ubuntu 16.04
* Python 3.5.2
* Flask 0.11.1
* Jinja2 2.8
* Bootstrap 3.3.7

CONFIG
-----

For all configuration, please check this **[config.py](flaskblog/config.py)**


BASIC AUTHENTICATION USING HTTP-AUTH
-----

```
/admin
/logout
```

INSTALL
-----

I assume you already setup your mongodb & flask development enviroment (pip, virtualenv, git, etc...). If not yet, going to search on Google.

**1. Create virtual enviroment and activate it.**

```
$ virtualenv --python=/usr/bin/python3 yourenv
$ source bin/activate
```

> `$ python` --> to check it, makesure your python version going to python3.


**2. Cloning this project**

```
$ git clone git@gitlab.com:agusmakmun/flaskblog.git
```

**3. Install all requirements**

```
$ pip install -r requirements.txt
```

-----

#### * Explanation of requirements


**1. `pip install Flask`**

```
click==6.6
Flask==0.11.1
itsdangerous==0.24
Jinja2==2.8
MarkupSafe==0.23
pkg-resources==0.0.0
Werkzeug==0.11.11
```

**2. `pip install flask-mongoengine`**

```
flask-mongoengine==0.8
Flask-WTF==0.12
mongoengine==0.10.6
pymongo==3.3.0
WTForms==2.1
```

**3. `pip install Flask-Script`**

```
Flask-Script==2.0.5
```

**4. `pip install flask-peewee`**

```
flask-peewee==0.6.7
peewee==2.8.3
wtf-peewee==0.2.6
```

------

So, we completely requirements you also can checkout at **[requirements.txt](requirements.txt)**.