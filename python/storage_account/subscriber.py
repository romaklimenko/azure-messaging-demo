# pylint: disable=missing-module-docstring
import os

import dotenv
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueClient

dotenv.load_dotenv()

try:
    STORAGE_ACCOUNT = os.environ["STORAGE_ACCOUNT"]
    QUEUE_NAME = "queue1"
    
    queue_client = QueueClient(
        f"https://{STORAGE_ACCOUNT}.queue.core.windows.net",
        queue_name=QUEUE_NAME,
        credential=DefaultAzureCredential())

    with queue_client:
        while True:
            messages = queue_client.receive_messages()
            for message in messages:
                print(f"Received a message: {message.content}")
                queue_client.delete_message(message)

except KeyboardInterrupt:
    print("Bye...")
# pylint: disable=broad-except
except Exception as ex:
    print(f"Exception: {ex}")
