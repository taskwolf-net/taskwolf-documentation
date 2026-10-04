ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/taskwolf-obfuscation:latest AS builder

RUN mkdir -p /home/taskwolf/documentation
RUN ln -s /obfuscation /home/taskwolf/documentation

COPY static /home/taskwolf/documentation/static
COPY obfuscation /home/taskwolf/documentation/obfuscation

ENV OBFUSCATION_HOME=/home/taskwolf/documentation

RUN node /home/taskwolf/documentation/obfuscation/obfuscate.js

FROM nginx

ARG SERVER_NAME
ENV SERVER_NAME=${SERVER_NAME}

COPY --from=builder /home/taskwolf/documentation/static /home/taskwolf/documentation/static/

COPY proxy/nginx.conf /etc/nginx/nginx.conf
COPY proxy/proxy /etc/nginx/sites-available/proxy
RUN mkdir -p /etc/nginx/sites-enabled
RUN ln -sf /etc/nginx/sites-available/proxy /etc/nginx/sites-enabled/proxy

CMD ["/bin/sh", "-c", "envsubst '$SERVER_NAME' < /etc/nginx/sites-available/proxy > /tmp/proxy && mv /tmp/proxy /etc/nginx/sites-available/proxy && exec nginx -g 'daemon off;'"]
