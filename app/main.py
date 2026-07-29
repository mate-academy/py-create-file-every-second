from datetime import datetime
from time import sleep


def main() -> None:
    """Create a file every second with timestamp."""
    while True:
        # Get current timestamp
        now = datetime.now()

        # Format timestamp as string for file content
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")

        # Create filename in the required format
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # Create and write to file
        with open(filename, "w") as f:
            f.write(timestamp_str)

        # Print to console
        print(f"{timestamp_str} {filename}")

        # Wait for 1 second
        sleep(1)


if __name__ == "__main__":
    main()
