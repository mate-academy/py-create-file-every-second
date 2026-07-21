from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        # Get current timestamp
        current_time = datetime.now()

        # Create filename in required format
        filename = (
            f"app-{current_time.hour}"
            f"_{current_time.minute}_"
            f"{current_time.second}.log"
        )

        # Write timestamp to file
        with open(filename, "w") as f:
            f.write(str(current_time))

        # Print timestamp and filename to console
        print(f"{current_time} {filename}")

        # Wait for 1 second before next iteration
        sleep(1)


if __name__ == "__main__":
    main()
