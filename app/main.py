from datetime import datetime
from time import sleep
import os

try:
    while True:
        # Get current timestamp
        timestamp = datetime.now()

        # Format file name
        file_name = f"app-{timestamp.hour}_{timestamp.minute}_{timestamp.second}.log"

        # Write the timestamp to the file
        with open(file_name, "w") as file:
            file.write(str(timestamp))

        # Print the output to console
        print(f"{timestamp} {file_name}")

        # Wait for 1 second
        sleep(1)
except KeyboardInterrupt:
    print("\nProcess terminated by user.")
