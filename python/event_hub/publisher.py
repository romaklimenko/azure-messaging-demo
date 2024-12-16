# pylint: disable=missing-module-docstring
import json
import os

import dotenv
from azure.eventhub import EventData, EventHubProducerClient
from azure.identity import DefaultAzureCredential

dotenv.load_dotenv()

EVENT_HUB_NAMESPACE = os.environ["EVENT_HUB_NAMESPACE"]
EVENT_HUB = os.environ["EVENT_HUB"]

producer = EventHubProducerClient(
    fully_qualified_namespace=f"{EVENT_HUB_NAMESPACE}.servicebus.windows.net",
    eventhub_name=EVENT_HUB,
    credential=DefaultAzureCredential())

with producer:
    batch = producer.create_batch()

    for i in range(10):
        batch.add(EventData(json.dumps({"message": i})))
        print(f"Message {i} added to the batch")

    producer.send_batch(batch)
    print("Batch sent")

print("Bye...")
