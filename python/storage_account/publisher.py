# pylint: disable=missing-module-docstring
import os
import time
import uuid

import dotenv
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueClient

dotenv.load_dotenv()

try:
    QUEUE_NAME = "queue1"
    PUBLISHER_ID = str(uuid.uuid4())
    print(f"Publisher ID: {PUBLISHER_ID}")

    queue_client = QueueClient(
        f"https://{os.environ['STORAGE_ACCOUNT_NAME']}.queue.core.windows.net",
        queue_name=QUEUE_NAME,
        credential=DefaultAzureCredential())

    i = 0

    while True:
        i += 1
        queue_client.send_message(
            {"publisher_id": PUBLISHER_ID, "message": i})
        print(f'Message {i} sent by Publisher {PUBLISHER_ID}')
        time.sleep(1)

except KeyboardInterrupt:
    print("Bye...")
# pylint: disable=broad-except
except Exception as ex:
    print(f"Exception: {ex}")
