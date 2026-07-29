from datetime import datetime
from time import sleep

while True:
    # Get the current timestamp
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    # Create the file name
    file_name = f"app-{now.hour}_{now.min}_{now.second}.log"

    # Write the timestamp to the file
    with open(file_name, "w") as file:
        file.write(timestamp)

    # Print the timestamp and file name
    print(f"{timestamp} {file_name}")

    # Wait for 1 second
    sleep(1)
