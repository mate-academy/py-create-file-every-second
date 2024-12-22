from datetime import datetime
import time

while True:
    # Get the current timestamp
    current_time = datetime.now()

    # Format the filename based on current time
    file_name = (f"app-{current_time.hour}_{current_time.minute}_"
                 f"{current_time.second}.log")

    # Open the file in write mode and write the timestamp
    with open(file_name, "w") as file:
        file.write(current_time.isoformat())

    # Print the timestamp and the file name
    print(f"{current_time.isoformat()} {file_name}")

    # Wait for 1 second before creating the next file
    time.sleep(1)
