<div align="center">
  <img src="https://dulno.com/static/img/logo-light.webp" alt="logo" width="128"  height="auto" />

  <h1><b>Dulno - Documentation</b><br><br></h1>

</div>

This repository contains the Dulno documentation website. It introduces the user to some functions and offers customers a contact point where they can get their questions answered.

## Status

|      | Pipeline status                                                               |
|------|-------------------------------------------------------------------------------|
| main | ![](https://git.dulno.com/dulno/dulno-documentation/badges/main/pipeline.svg) |
| dev  | ![](https://git.dulno.com/dulno/dulno-documentation/badges/dev/pipeline.svg)  |

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