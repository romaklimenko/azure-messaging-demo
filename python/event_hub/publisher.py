# pylint: disable=missing-module-docstring
import json
import os
import time

import dotenv
from azure.eventhub import EventData, EventHubProducerClient
from azure.identity import DefaultAzureCredential

dotenv.load_dotenv()

try:

    EVENT_HUB_NAMESPACE = os.environ['EVENT_HUB_NAMESPACE']
    EVENT_HUB = os.environ["EVENT_HUB"]

    producer = EventHubProducerClient(
        fully_qualified_namespace=f"{
            EVENT_HUB_NAMESPACE}.servicebus.windows.net",
        eventhub_name=EVENT_HUB,
        credential=DefaultAzureCredential())

    with producer:
        i = 0
        batch = producer.create_batch()
        while True:
            message = {"message": (i := i + 1)}
            batch.add(EventData(json.dumps(message)))
            if i % 10 == 0:
                producer.send_batch(batch)
                print(f"Batch {batch} is sent.")
                batch = producer.create_batch()
                time.sleep(10)

except KeyboardInterrupt:
    print("Bye...")
# pylint: disable=broad-except
except Exception as ex:
    print(f"Exception: {ex}")
