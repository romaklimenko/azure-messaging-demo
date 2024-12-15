# pylint: disable=missing-module-docstring
import os
import uuid

import dotenv
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueClient

dotenv.load_dotenv()

try:
    QUEUE_NAME = "queue1"
    SUBSCRIBER_ID = str(uuid.uuid4())
    print(f"Subscriber ID: {SUBSCRIBER_ID}")

    queue_client = QueueClient(
        f"https://{os.environ['STORAGE_ACCOUNT']}.queue.core.windows.net",
        queue_name=QUEUE_NAME,
        credential=DefaultAzureCredential())

    while True:
        messages = queue_client.receive_messages()
        for message in messages:
            print(f"Subscriber {SUBSCRIBER_ID} received a message: {
                message.content}")
            queue_client.delete_message(message)

except KeyboardInterrupt:
    print("Bye...")
# pylint: disable=broad-except
except Exception as ex:
    print(f"Exception: {ex}")
