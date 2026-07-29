from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        # Get current time
        current_time = datetime.now()
        # Format the file name according to current time
        file_name = current_time.strftime("app-%H_%M_%S.log")
        # Format the content for the file without microseconds
        file_content = current_time.strftime("%Y-%m-%d %H:%M:%S")

        # Create and write to the file
        with open(file_name, "w") as file:
            file.write(file_content)

        # Print to console
        print(f"{file_content} {file_name}")

        # Sleep for 1 second
        time.sleep(1)


if __name__ == "__main__":
    main()
