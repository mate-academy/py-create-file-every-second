from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()

        # Format for file content (timestamp): 2007-06-29 13:49:40
        timestamp_content = current_time.strftime("%Y-%m-%d %H:%M:%S")

        # Create and write to the file
        with open(current_time.strftime("app-%H_%M_%S.log"), "w") as f:
            f.write(timestamp_content)

        # Print to console: timestamp and newly created file name
        print(
            f"{timestamp_content} "
            f"{current_time.strftime('app-%H_%M_%S.log')}")

        # Wait for 1 second before the next iteration
        sleep(1)


if __name__ == "__main__":
    main()
