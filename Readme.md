# DOCKER(Kafka-Pyspark)
This is an integration of Kafka with Pyspark using Docker containers.

Start the process with:
```
docker compose up -d
```
List all topics via:
```
docker exec -it broker kafka-topics \
	--list \
	--bootstrap-server localhost:9092
```
Listen to test_topic via:
```
docker exec -ti broker kafka-console-consumer \
	--topic test_topic \
	--bootstrap-server localhost:9092
```
Listen to output_topic_sink via:
```
docker exec -ti broker kafka-console-consumer \
	--topic output_topic_sink \
	--bootstrap-server localhost:9092
```
View all messages that have been sent to a topic via:
```
docker exec -ti broker kafka-console-consumer \
    --topic test_topic \
	--bootstrap-server localhost:9092 \
	--from-beginning
```
We can also manually send events to a topic via:

```
docker exec -ti broker kafka-console-producer \
	--topic test_topic \
	--bootstrap-server broker:9092
```
View logs of any container via:
```
docker compose logs -f producer
```
```
docker compose logs -f pyspark_consumer
```