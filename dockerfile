FROM python:3.8

RUN apt-get update && \
    apt-get install -y --no-install-recommends sshpass && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /data

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip  && pip install --no-cache-dir -r /app/requirements.txt

COPY ./app /app
COPY ./data /app

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]