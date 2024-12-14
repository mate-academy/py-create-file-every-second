from datetime import datetime
import time

while True:
    # Get current timestamp
    current_time = datetime.now()

    # Format the filename and the timestamp
    file_name = current_time.strftime("app-%H_%M_%S.log")
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")

    with open(file_name, "w") as f:
        f.write(timestamp)

    # Print the timestamp and the newly created file name
    print(f"{timestamp} {file_name}")

    # Wait for 1 second before the next iteration
    time.sleep(1)
