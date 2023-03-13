FROM ubuntu:22.10

RUN apt-get update
RUN apt-get install net-tools

RUN mkdir /.hidden

WORKDIR /.hidden

COPY check.sh .
COPY flag .

RUN chmod +x ./check.sh

CMD ["./check.sh"]