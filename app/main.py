from datetime import datetime
from time import sleep

try:
    while True:
        # Get the current timestamp
        current_time = datetime.now()

        # Format the file name
        file_name = (
            f"app-{current_time.hour}_"
            f"{current_time.minute}_"
            f"{current_time.second}.log"
        )

        # Write the timestamp into the file
        with open(file_name, "w") as file:
            file.write(str(current_time))

        # Print the timestamp and file name to the console
        print(f"{current_time} {file_name}")

        # Wait for 1 second
        sleep(1)

except KeyboardInterrupt:
    print("\nProcess terminated by user.")
