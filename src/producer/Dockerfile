FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY producer.py .

COPY indexProcessed.csv .

ENV KAFKA_BOOTSTRAP_SERVERS='broker:29092'
ENV INPUT_TOPIC='test_topic'

CMD ["python", "producer.py"]
