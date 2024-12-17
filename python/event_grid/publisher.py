# pylint: disable=missing-module-docstring
import os
import time

import dotenv
from azure.eventgrid import EventGridPublisherClient
from azure.identity import DefaultAzureCredential

dotenv.load_dotenv()

try:
    EVENT_GRID_HOST_NAME = os.environ["EVENT_GRID_HOST_NAME"]
    EVENT_GRID_TOPIC = os.environ["EVENT_GRID_TOPIC"]

    publisher = EventGridPublisherClient(
        endpoint=f"https://{EVENT_GRID_HOST_NAME}",
        namespace_topic=EVENT_GRID_TOPIC,
        credential=DefaultAzureCredential()
    )

    with publisher:
        i = 0
        while True:
            event = {
                "id": str(i := i + 1),
                "source": "python",
                "specversion": "1.0",
                "type": "event",
                "data": {"message": f"{i}"}
            }
            publisher.send(event)
            print(f"Event {i} is sent")
            if i % 10 == 0:
                time.sleep(10)

except KeyboardInterrupt:
    print("Bye...")
# pylint: disable=broad-except
except Exception as ex:
    print(f"Exception: {ex}")
