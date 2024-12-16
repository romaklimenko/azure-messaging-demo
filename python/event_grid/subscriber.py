# pylint: disable=missing-module-docstring
import os

import dotenv
from azure.eventgrid import EventGridConsumerClient
from azure.identity import DefaultAzureCredential

dotenv.load_dotenv()

EVENT_GRID_HOST_NAME = os.getenv("EVENT_GRID_HOST_NAME")
EVENT_GRID_TOPIC = os.getenv("EVENT_GRID_TOPIC")

consumer = EventGridConsumerClient(
    endpoint=f'https://{EVENT_GRID_HOST_NAME}',
    namespace_topic=EVENT_GRID_TOPIC,
    subscription='eventGridSubscription1',
    credential=DefaultAzureCredential()
)

with consumer:
    for event in consumer.receive():
        print(event)

print("Bye...")
