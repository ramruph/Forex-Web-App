from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'price_data_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_serializer=lambda v: json.loads(v.decode('utf-8'))
)

for message in consumer:
    print(f"Received message: {message.value}")
