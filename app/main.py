from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    try:
        while True:
            # Get the current timestamp
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

            # Format the file name
            file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

            # Write the timestamp to the file
            with open(file_name, "w") as file:
                file.write(timestamp)

            # Print confirmation
            print(f"{timestamp} {file_name}")

            # Wait for 1 second
            time.sleep(1)
    except KeyboardInterrupt:
        raise KeyboardInterrupt


if __name__ == "__main__":
    main()
