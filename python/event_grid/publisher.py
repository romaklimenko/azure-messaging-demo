# pylint: disable=missing-module-docstring
import os

import dotenv
from azure.eventgrid import EventGridPublisherClient
from azure.identity import DefaultAzureCredential

dotenv.load_dotenv()

EVENT_GRID_HOST_NAME = os.getenv("EVENT_GRID_HOST_NAME")
EVENT_GRID_TOPIC = os.getenv("EVENT_GRID_TOPIC")

publisher = EventGridPublisherClient(
    endpoint=f'https://{EVENT_GRID_HOST_NAME}',
    namespace_topic=EVENT_GRID_TOPIC,
    credential=DefaultAzureCredential()
)

with publisher:
    for i in range(10):
        event = {
            "id": str(i),
            "source": "python",
            "specversion": "1.0",
            "type": "event",
            "data": {
                    "message": f"Event {i} from Python"
            }
        }
        publisher.send(event)
        print(f"Event {i} sent")
    print(f"{i + 1} events sent")

print("Bye...")
