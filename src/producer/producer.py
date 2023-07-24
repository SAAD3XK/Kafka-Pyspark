from confluent_kafka import Producer
from time import sleep
from json import dumps
import pandas as pd
import json
import os

bootstrap_servers = os.environ.get('KAFKA_BOOTSTRAP_SERVERS')
topic_name = os.environ.get('INPUT_TOPIC')

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()}')

def main():
    producer_config = {
        'bootstrap.servers': bootstrap_servers    }
    producer = Producer(producer_config)
    df = pd.read_csv('indexProcessed.csv')
    while True:
        sending_data = df.sample(1).to_dict(orient="records")[0]
        producer.produce(topic_name, value=json.dumps(sending_data).encode("utf-8"), callback=delivery_report)
        producer.poll(0.5)
        print("Sending dataframe sample...")
        sleep(5)

if __name__ == '__main__':
    main()
