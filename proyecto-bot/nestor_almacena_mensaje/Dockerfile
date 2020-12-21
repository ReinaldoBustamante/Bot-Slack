FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27025

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_almacena_mensaje

COPY ./nestor_almacena_mensaje.py /nestor_almacena_mensaje.py

CMD [ "python", "/nestor_almacena_mensaje.py" ]
