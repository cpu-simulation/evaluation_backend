FROM python:3.10-slim-bullseye

RUN apt-get update

RUN \
  apt-get install -y --no-install-recommends --no-install-suggests \
  python3-dev build-essential default-libmysqlclient-dev pkg-config\
  && pip install --no-cache-dir --upgrade pip


WORKDIR /app

COPY req.pip /app

RUN export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`

RUN export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags`

RUN pip install --no-cache-dir --requirement /app/req.pip

COPY . .

EXPOSE 8000
WORKDIR /app/rest_service
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

