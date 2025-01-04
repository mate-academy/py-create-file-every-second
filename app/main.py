import os
from datetime import datetime
from time import sleep

try:
    while True:
        # Get the current timestamp
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")

        # Generate the file name
        file_name = f"app-{now.strftime('%H_%M_%S')}.log"

        # Write the timestamp to the file
        with open(file_name, "w") as file:
            file.write(timestamp)

        # Print success message to the console
        print(f"Created file: {file_name} with timestamp: {timestamp}")

        # Wait for 1 second
        sleep(1)
except KeyboardInterrupt:
    print("\nProgram terminated.")
