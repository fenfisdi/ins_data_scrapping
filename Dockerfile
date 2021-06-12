FROM python:3.8-slim-buster

EXPOSE 8080

ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app

COPY requirements.txt .

RUN pip install --no-cache-dir -U pip \
    && pip install git+https://gitlab.com/hubrain/covid19.git \
    && pip install --no-cache-dir -r requirements.txt

WORKDIR ${APP_HOME}

COPY src src
COPY main.py .
COPY docker-entrypoint.sh .

ENTRYPOINT ["/bin/bash"]
CMD ["./docker-entrypoint.sh"]
