FROM python:3.6.4

ARG GEOCODER_PORT
ARG GOOGLE_API_KEY
ARG GEOCODER_HOST
ENV GEOCODER_PORT=${GEOCODER_PORT}
ENV GOOGLE_API_KEY=${GOOGLE_API_KEY}
ENV GEOCODER_HOST=${GEOCODER_HOST}

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE ${GEOCODER_PORT}

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]
