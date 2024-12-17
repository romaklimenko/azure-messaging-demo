# pylint: disable=missing-module-docstring
import json
import os
import time

import dotenv
from azure.identity import DefaultAzureCredential
from azure.servicebus import ServiceBusClient, ServiceBusMessage

dotenv.load_dotenv()

try:
    SERVICE_BUS_NAMESPACE = os.environ["SERVICE_BUS_NAMESPACE"]
    TOPIC_NAME = "topic1"

    servicebus_client = ServiceBusClient(
        f"sb://{SERVICE_BUS_NAMESPACE}.servicebus.windows.net",
        credential=DefaultAzureCredential())

    topic_sender = servicebus_client.get_topic_sender(topic_name=TOPIC_NAME)

    with servicebus_client, topic_sender:
        i = 0
        batch = topic_sender.create_message_batch()
        while True:
            message = {"message": (i := i + 1)}
            batch.add_message(ServiceBusMessage(json.dumps(message)))
            if i % 10 == 0:
                topic_sender.send_messages(batch)
                print(f"Messages in a batch {batch} are sent to topic1.")
                batch = topic_sender.create_message_batch()
                time.sleep(10)

except KeyboardInterrupt:
    print("Bye...")
# pylint: disable=broad-except
except Exception as ex:
    print(f"Exception: {ex}")
