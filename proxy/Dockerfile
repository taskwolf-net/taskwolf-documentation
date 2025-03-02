ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-obfuscation:latest AS builder

RUN mkdir -p /home/dulno/documentation
RUN ln -s /obfuscation /home/dulno/documentation

COPY static /home/dulno/documentation/static
COPY obfuscation /home/dulno/documentation/obfuscation

ENV OBFUSCATION_HOME=/home/dulno/documentation

RUN node /home/dulno/documentation/obfuscation/obfuscate.js

FROM nginx

ARG SERVER_NAME
ENV SERVER_NAME=${SERVER_NAME}

COPY --from=builder /home/dulno/documentation/static /home/dulno/documentation/static/

COPY proxy/nginx.conf /etc/nginx/nginx.conf
COPY proxy/proxy /etc/nginx/sites-available/proxy
RUN mkdir -p /etc/nginx/sites-enabled
RUN ln -sf /etc/nginx/sites-available/proxy /etc/nginx/sites-enabled/proxy

CMD ["/bin/sh", "-c", "envsubst '$SERVER_NAME' < /etc/nginx/sites-available/proxy > /tmp/proxy && mv /tmp/proxy /etc/nginx/sites-available/proxy && exec nginx -g 'daemon off;'"]
