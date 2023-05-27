FROM python:3.10.11-slim-buster


ARG arg_time=$arg_time

ENV SLEEP_TIME=$SLEEP_TIME


WORKDIR code/

RUN mkdir test
RUN touch some_test.txt
RUN echo "Sleep $arg_time"


CMD sleep $SLEEP_TIME

