# app/main.py
from datetime import datetime
from time import sleep


def create_file() -> None:
    """
    This function creates a file with a timestamp every second.
    The filename depends on the current time.
    """
    while True:
        # Get the current time
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # Write the timestamp to the file
        with open(file_name, "w") as log_file:
            log_file.write(timestamp)

        # Print information about the created file
        print(f"{timestamp} -> {file_name}")

        # Wait 1 second before creating the next file
        sleep(1)


def main() -> None:
    """
    Main function to start the file creation process.
    """
    create_file()


if __name__ == "__main__":
    main()
