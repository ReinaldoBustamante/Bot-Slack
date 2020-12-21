FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-1503558912048-1503647302688-S8gMS2WW3KtHLPnkohDPl1cQ"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /nestor_slack_writer

COPY ./nestor_slack_writer.py /nestor_slack_writer.py
COPY ./nestor_slack_writer.py /nestor_slack_writer.py

CMD [ "python", "/nestor_slack_writer.py" ]
