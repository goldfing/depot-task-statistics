# depot-task-statistics
Realtime Data Stream Analysis (Python + Kafka + Cassandra)

## Data Specification
1. Depot : Area_1 ~ 5
2. Task Status : PENDING / INPROGRESS / DONE

## Log Column Information
1. depot
2. task_no
3. worker
4. task_status
5. trackedAt

## Python Modules
1. Kafka-Python : pip3 install kafka-python
2. Cassandra-driver : pip3 install cassandra-driver

## Kafka
### Topic Create

./kafka-topics.sh --create --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1  --topic depot.task.status.log.1

## Execute
Publisher
./task_publisher.py

Subscriber
./daily_task_status.py

## Statistics Element
1. Count of each task status of the depot
2. List of each task status of the depot
