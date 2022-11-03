FROM python:3.9

WORKDIR /todolist

COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends \
#    gcc \
    curl
#    build-essential \
#    libpq-dev
RUN apt-get autoclean && apt-get autoremove
RUN rm -rf /var/lib/apt/lists/* /tmp /var/tmp
RUN pip install -r requirements.txt
# Копируем код приложения
COPY app/ .
COPY migrations migrations
