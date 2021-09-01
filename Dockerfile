FROM alpine:3.13
MAINTAINER me-docker@ela.build

RUN apk --no-cache add python3 py3-pip && pip install --upgrade pip

COPY . /app
WORKDIR /app

RUN pip install -r /app/requirements.txt
RUN pip install gunicorn

EXPOSE 8000
CMD ["gunicorn", "-b 0.0.0.0", "-w 2", "hello:app"]
