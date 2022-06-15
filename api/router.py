from fastapi import APIRouter
from schema import Message
from conf import loop, KAFKA_BOOTSTRAP_SERVER, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import json


router = APIRouter()


@router.post('/create_message')
async def send(message:Message):
    producer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVER)
    await producer.start()
    try:
        print(f"Sending message with value: {message}")
        value_json = json.dumps(message.__dict__).encode('utf-8')
        await producer.send_and_wait(topic=KAFKA_TOPIC, value=value_json)
    finally:
        await producer.stop()


async def consume():
    consumer = AIOKafkaConsumer(KAFKA_TOPIC, loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVER, group_id=KAFKA_CONSUMER_GROUP)
    await consumer.start()
    try:
        async for msg in consumer:
            print(F"Consumer message: {msg}")
    finally:
        await consumer.stop()
