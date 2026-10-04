# Dulno - Documentation

[![CI](https://github.com/taskwolf-net/taskwolf-documentation/actions/workflows/ci.yml/badge.svg)](https://github.com/taskwolf-net/taskwolf-documentation/actions/workflows/ci.yml)

This repository contains the Dulno documentation website. It introduces the user to some functions and offers customers a contact point where they can get their questions answered.

## Installation

```bash
python -m venv env

source env/bin/activate

pip install django gunicorn django-cors-headers requests jwt

django-admin compilemessages

gunicorn --config app/gunicorn-config.py app.wsgi
```

## Run

```bash
source env/bin/activate

gunicorn --config app/gunicorn-config.py app.wsgi
```

## Compile locales

```bash
django-admin compilemessages
```