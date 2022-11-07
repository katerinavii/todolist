FROM python:3.10

WORKDIR /opt/todolist

COPY ../requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl
RUN apt-get autoclean && apt-get autoremove
RUN rm -rf /var/lib/apt/lists/* /tmp /var/tmp
RUN pip install -r requirements.txt
# Копируем код приложения и миграции
COPY app/ .
#COPY migrations migrations

ENTRYPOINT ["bash", "entrypoint.sh"]
