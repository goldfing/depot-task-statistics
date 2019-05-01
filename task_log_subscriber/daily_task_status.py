# -*- coding:utf-8 -*-

from kafka import KafkaConsumer
from config.kafka_config import kafka_config

from cassandra.cluster import Cluster
import json

kafkaConfig = kafka_config()

consumer = KafkaConsumer(bootstrap_servers=kafkaConfig.bootstrap_servers,
                         auto_offset_reset='earliest',
                         consumer_timeout_ms=1000,
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

consumer.subscribe([kafkaConfig.topic])


cluster = Cluster() # Initialize Cassandra
session = cluster.connect("depot_task_statistics")

for msg in consumer:
    consumeValue = json.loads(msg.value)

    upd_query = "UPDATE daily_task_status_count " \
                "SET task_count=task_count+1 " \
                "WHERE " \
                "task_date='{0}' " \
                "AND depot='{1}' " \
                "AND task_status='{2}'"\
        .format(consumeValue['trackedAt'][0:10], consumeValue['depot'], consumeValue['task_status'])
    session.execute(upd_query)

    list_query = "UPDATE daily_task_status_list " \
                 "SET task_no_list=task_no_list + ['{0}'] " \
                 "WHERE " \
                 "task_date='{1}' " \
                 "AND depot='{2}' " \
                 "AND task_status='{3}'"\
        .format(consumeValue['task_no'], consumeValue['trackedAt'][0:10], consumeValue['depot'], consumeValue['task_status'])
    session.execute(list_query)

consumer.close()
