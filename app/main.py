from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        # Get current time
        now = datetime.now()

        # Create filename in format: app-{hours}_{minutes}_{seconds}.log
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # Create file content as timestamp
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        try:
            # Create and write to the file
            with open(filename, "w") as f:
                f.write(timestamp)

            # Print success message to console
            print(f"{timestamp} {filename}")

        except Exception as e:
            print(f"Error creating file {filename}: {e}")

        # Wait for 1 second before next iteration
        sleep(1)


if __name__ == "__main__":
    main()
