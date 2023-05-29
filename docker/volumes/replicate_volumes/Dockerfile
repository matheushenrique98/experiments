FROM python:3.12.0b1-slim-buster

WORKDIR anothertest/

COPY entrypoint.sh ./

# Some version Docker introduce a bug when generate .sh in Windows and use it in a Unix image docker
# So the purporse dos2unix is to correct
RUN apt-get update && apt-get install -y dos2unix
RUN dos2unix entrypoint.sh

CMD ["bash", "entrypoint.sh"]
