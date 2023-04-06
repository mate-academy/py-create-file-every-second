from time import sleep
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        # Create filename with the required format
        filename = f"app-{datetime.now().strftime('%H_%M_%S')}.log"

        # Get current timestamp
        timestamp = str(datetime.now())

        # Write timestamp to file
        with open(filename, "w") as f:
            f.write(timestamp)

        # Print timestamp and filename to console
        print(timestamp, filename)

        # Wait for 1 second before creating the next file
        sleep(1)


if __name__ == "__main__":
    main()
