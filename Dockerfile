FROM docker.io/python:3.11-buster
LABEL maintainer="Ata Noor <>ataulnoor75@gmail.com"

WORKDIR /app
ADD ./ /app/
COPY ./requirements.txt requirements.txt
RUN apt-get -yq update && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/

CMD [ "gunicorn", "--bind", "0.0.0.0:8080", "--log-level", "info", "--access-logfile", "-", "app:app" ]