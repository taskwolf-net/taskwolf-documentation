ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-obfuscation:latest AS builder

RUN mkdir -p /home/dulno/documentation
RUN ln -s /obfuscation /home/dulno/documentation

COPY static /home/dulno/documentation/static
COPY obfuscation /home/dulno/documentation/obfuscation

ENV OBFUSCATION_HOME=/home/dulno/documentation

RUN node /home/dulno/documentation/obfuscation/obfuscate.js

FROM nginx

COPY --from=builder /home/dulno/documentation/static /home/dulno/documentation/static/

COPY proxy/nginx.conf /etc/nginx/nginx.conf
COPY proxy/proxy /etc/nginx/sites-available/proxy
COPY proxy/proxy /etc/nginx/sites-enabled/proxy
