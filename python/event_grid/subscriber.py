# pylint: disable=missing-module-docstring
import os

import dotenv
from azure.eventgrid import EventGridConsumerClient
from azure.identity import DefaultAzureCredential

dotenv.load_dotenv()

try:
    EVENT_GRID_HOST_NAME = os.environ["EVENT_GRID_HOST_NAME"]
    EVENT_GRID_TOPIC = os.environ["EVENT_GRID_TOPIC"]
    SUBSCRIPTION = "eventGridSubscription1"

    consumer = EventGridConsumerClient(
        endpoint=f'https://{EVENT_GRID_HOST_NAME}',
        namespace_topic=EVENT_GRID_TOPIC,
        subscription=SUBSCRIPTION,
        credential=DefaultAzureCredential()
    )

    with consumer:
        lock_tokens = []
        while True:
            for event in consumer.receive():
                print(f"Event received: {event}.")
                lock_tokens.append(event.broker_properties.lock_token)

                if len(lock_tokens) >= 10:
                    consumer.acknowledge(lock_tokens=lock_tokens)
                    print(f"Events acknowledged {lock_tokens}.")
                    lock_tokens.clear()

except KeyboardInterrupt:
    print("Bye...")
# pylint: disable=broad-except
except Exception as ex:
    print(f"Exception: {ex}")
