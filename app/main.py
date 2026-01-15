from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        # Get current timestamp
        now = datetime.now()
        timestamp_str = now.strftime("%Y-%m-%d "
                                     "%H:%M:%S")  # Removed microseconds

        # Format file name
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # Write timestamp to file
        with open(file_name, "w") as file:
            file.write(timestamp_str)

        # Print output to console
        print(f"{timestamp_str} {file_name}")

        # Sleep for 1 second
        time.sleep(1)


if __name__ == "__main__":
    main()
