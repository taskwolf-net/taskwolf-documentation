FROM registry.dulno.com/dulno-obfuscation:latest AS builder

RUN ln -s /obfuscation /documentation

COPY . /documentation

WORKDIR /documentation

ENV OBFUSCATION_HOME=/documentation

RUN node obfuscation/obfuscate.js

FROM python:3

RUN apt-get update && apt-get install -y gettext && apt-get clean

RUN pip install django
RUN pip install gunicorn
RUN pip install django-cors-headers
RUN pip install requests
RUN pip install jwt

COPY --from=builder /documentation /documentation

WORKDIR /documentation

RUN django-admin compilemessages

ENTRYPOINT ["gunicorn", "--config", "app/gunicorn-config.py", "app.wsgi"]