from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep
from typing import NoReturn


def main() -> NoReturn:
    while True:
        # Get the current datetime for both filename and file content
        timestamp = datetime.now()

        # Format the timestamp without microseconds
        formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        # Create file name with the required format
        file_name = timestamp.strftime("app-%H_%M_%S.log")

        # Write the formatted time to the file
        with open(file_name, "w") as file:
            file.write(formatted_time)

        # Print the output to console as specified
        print(f"{formatted_time} {file_name}")

        # Wait for 1 second before creating the next file
        sleep(1)


if __name__ == "__main__":
    main()
