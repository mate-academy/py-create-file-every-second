from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        # Get the current timestamp
        timestamp = datetime.now()

        # Format file name as specifies
        file_name = (f"app-{timestamp.hour}_{timestamp.minute}"
                     f"_{timestamp.second}.log")

        # Write timestamp to the file
        with open(file_name, "w") as file:
            file.write(str(timestamp))

        # Print timestamp and file name to console
        print(f"{timestamp} {file_name}")

        # Wait for 1 second before creating the next file
        sleep(1)


if __name__ == "__main__":
    main()
