# pylint: disable=missing-module-docstring
import os

import dotenv
from azure.identity import DefaultAzureCredential
from azure.servicebus import ServiceBusClient

dotenv.load_dotenv()

SERVICE_BUS_NAMESPACE = os.environ["SERVICE_BUS_NAMESPACE"]

servicebus_client = ServiceBusClient(
    f"sb://{SERVICE_BUS_NAMESPACE}.servicebus.windows.net",
    credential=DefaultAzureCredential())

subscription_receiver = servicebus_client.get_subscription_receiver(
    topic_name="topic1", subscription_name="subscription2")

with subscription_receiver:
    for message in subscription_receiver:
        print(f"Received: {message}")
        subscription_receiver.complete_message(message)

print("Bye...")
