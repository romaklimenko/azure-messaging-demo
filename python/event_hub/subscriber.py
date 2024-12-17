# pylint: disable=missing-module-docstring
import os

import dotenv
from azure.eventhub import EventHubConsumerClient, PartitionContext
from azure.identity import DefaultAzureCredential

dotenv.load_dotenv()

try:

    EVENT_HUB_NAMESPACE = os.environ["EVENT_HUB_NAMESPACE"]
    EVENT_HUB = os.environ["EVENT_HUB"]

    consumer = EventHubConsumerClient(
        fully_qualified_namespace=f"{
            EVENT_HUB_NAMESPACE}.servicebus.windows.net",
        eventhub_name=EVENT_HUB,
        consumer_group="$Default",
        credential=DefaultAzureCredential())

    # pylint: disable=missing-function-docstring
    def on_event_batch(partition_context: PartitionContext, events):
        for event in events:
            print(f"Received event: {event.body_as_str()}.")
        partition_context.update_checkpoint()

    with consumer:
        while True:
            consumer.receive_batch(on_event_batch=on_event_batch)

except KeyboardInterrupt:
    print("Bye...")
# pylint: disable=broad-except
except Exception as ex:
    print(f"Exception: {ex}")
