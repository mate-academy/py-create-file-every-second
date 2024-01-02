from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-7]

        # Create the file name in the specified format
        file_name = f"app-{datetime.now().strftime('%H_%M_%S')}.log"

        # Write the timestamp to the file
        with open(file_name, "w") as file:
            file.write(timestamp)

        # Print the timestamp and the newly created file name
        print(f"{timestamp} {file_name}")

        # Wait for 1 second before creating the next file
        sleep(1)

    # Run the function to create files indefinitely
    main()


if __name__ == "__main__":
    main()
