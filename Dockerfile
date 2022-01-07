FROM python:3.8.3-alpine

WORKDIR /usr/src/gachlat

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers && pip install Pillow

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
COPY . .

ENTRYPOINT ["/usr/src/gachlat/entrypoint.sh"]
