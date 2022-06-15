import asyncio

# env variables
KAFKA_BOOTSTRAP_SERVER = 'localhost:9093'
KAFKA_TOPIC = 'kafka'
KAFKA_CONSUMER_GROUP = 'group-id'
loop = asyncio.get_event_loop()