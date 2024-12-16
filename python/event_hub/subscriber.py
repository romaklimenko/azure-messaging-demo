# pylint: disable=missing-module-docstring
import os

import dotenv
from azure.eventhub import EventHubConsumerClient
from azure.identity import DefaultAzureCredential

dotenv.load_dotenv()

EVENT_HUB_NAMESPACE = os.environ["EVENT_HUB_NAMESPACE"]
EVENT_HUB = os.environ["EVENT_HUB"]

consumer = EventHubConsumerClient(
    fully_qualified_namespace=f"{EVENT_HUB_NAMESPACE}.servicebus.windows.net",
    eventhub_name=EVENT_HUB,
    consumer_group='$Default',
    credential=DefaultAzureCredential())

with consumer:
    consumer.receive(on_event=lambda _, event: print(
        f"Received event: {event.body_as_str()}.\n"))

print("Bye...")
