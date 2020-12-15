FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-1503558912048-1503647302688-vPFYZkn8lRp0kWzpaRDi5HnF"
ENV SLACK_SIGNING_SECRET="6f94fe718bbc6af37a931072df0fe318"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_slack_reader_2

COPY ./nestor_slack_reader_2.py /nestor_slack_reader_2.py

CMD [ "python", "/nestor_slack_reader_2.py" ]
