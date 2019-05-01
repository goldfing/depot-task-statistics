# -*- coding:utf-8 -*-

from kafka import KafkaProducer
import pandas as pd
import json
from time import sleep
from config.kafka_config import kafka_config

kafkaConfig = kafka_config()
producer = KafkaProducer(bootstrap_servers=kafkaConfig.bootstrap_servers,
                         acks=1,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Title : depot,task_no,worker,task_status,trackedAt
# Sample : Area_1,1,A1_W1,PENDING,2019-04-20 02:00:00
data_frame = pd.read_csv("task_logs-20190420.csv")

for i in range(data_frame["task_no"].count()):
    data = data_frame.iloc[[i]].to_json(orient="records")[1:-1]

    producer.send(topic=kafkaConfig.topic, value=data)

    print("{0} : {1}".format(i, data))
    sleep(0.5)

producer.close()
