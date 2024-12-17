# pylint: disable=missing-module-docstring
import os

import dotenv
from azure.identity import DefaultAzureCredential
from azure.servicebus import ServiceBusClient

dotenv.load_dotenv()

try:
    SERVICE_BUS_NAMESPACE = os.environ["SERVICE_BUS_NAMESPACE"]
    TOPIC_NAME = "topic1"
    SUBSCRIPTION_NAME = "subscription2"

    servicebus_client = ServiceBusClient(
        f"sb://{SERVICE_BUS_NAMESPACE}.servicebus.windows.net",
        credential=DefaultAzureCredential())

    subscription_receiver = servicebus_client.get_subscription_receiver(
        topic_name=TOPIC_NAME,
        subscription_name=SUBSCRIPTION_NAME)

    with servicebus_client, subscription_receiver:
        while True:
            for message in subscription_receiver:
                print(f"Received: {message}")
                subscription_receiver.complete_message(message)

except KeyboardInterrupt:
    print("Bye...")
# pylint: disable=broad-except
except Exception as ex:
    print(f"Exception: {ex}")
