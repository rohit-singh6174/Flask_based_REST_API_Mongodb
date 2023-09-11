FROM python:3-alpine3.11
WORKDIR /REST-API-Flask
ADD . /REST-API-Flask/
EXPOSE 5001
CMD python ./run.py
