# pylint: disable=missing-module-docstring
import json
import os

import dotenv
from azure.identity import DefaultAzureCredential
from azure.servicebus import ServiceBusClient, ServiceBusMessage

dotenv.load_dotenv()

SERVICE_BUS_NAMESPACE = os.environ["SERVICE_BUS_NAMESPACE"]

servicebus_client = ServiceBusClient(
    f"sb://{SERVICE_BUS_NAMESPACE}.servicebus.windows.net",
    credential=DefaultAzureCredential())

topic_sender = servicebus_client.get_topic_sender(topic_name="topic1")

for i in range(10):
    message = ServiceBusMessage(json.dumps({"message": i}))
    topic_sender.send_messages(message)
    print(f"Message {i} sent to topic1")

topic_sender.close()
servicebus_client.close()

print("Bye...")
