FROM python:3.7-alpine

COPY requirements.txt /

# RUN pip install -r /requirements.txt
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install -r requirements.txt \
    && apk del .build-deps gcc musl-dev

WORKDIR /app
COPY src/ src/
RUN mkdir logs
COPY run_server .

EXPOSE 5000

CMD ["./run_server"]
