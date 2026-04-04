from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()

        # Format parts
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # Create file and write timestamp
        with open(file_name, "w") as f:
            f.write(timestamp)

        # Print result
        print(f"{timestamp} {file_name}")

        # Wait 1 second
        sleep(1)


if __name__ == "__main__":
    main()
