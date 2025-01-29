FROM registry.dulno.com/dulno-obfuscation:latest AS builder

RUN mkdir -p /home/dulno/documentation
RUN ln -s /obfuscation /home/dulno/documentation

COPY static /home/dulno/documentation/static
COPY obfuscation /home/dulno/documentation/obfuscation

ENV OBFUSCATION_HOME=/home/dulno/documentation

RUN node /home/dulno/documentation/obfuscation/obfuscate.js

FROM alpine
COPY --from=builder /home/dulno/documentation/static /static/