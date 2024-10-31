import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        # Get the current timestamp
        now = datetime.now()

        # Format the file name with current time
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # Write the timestamp to the file
        with open(file_name, "w") as file:
            file.write(str(now))

        # Print the timestamp and the file name to console
        print(f"{now} {file_name}")

        # Wait for 1 second before creating the next file
        time.sleep(1)


if __name__ == "__main__":
    main()
