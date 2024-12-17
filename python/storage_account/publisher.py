# pylint: disable=missing-module-docstring
import os
import time

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
        i = 0
        while True:
            queue_client.send_message({"message": (i := i + 1)})
            print(f"Message {i} is sent.")
            if i % 10 == 0:
                time.sleep(10)

except KeyboardInterrupt:
    print("Bye...")
# pylint: disable=broad-except
except Exception as ex:
    print(f"Exception: {ex}")
