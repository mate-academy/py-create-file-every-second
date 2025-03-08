from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        # Get the current timestamp
        now = datetime.now()

        # Format the filename using hours, minutes, and seconds
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # Format the content as the current timestamp
        content = now.strftime("%Y-%m-%d %H:%M:%S")

        # Create the file and write the content
        with open(filename, "w") as file:
            file.write(content)

        # Print the timestamp and the newly created file name
        print(f"{content} {filename}")

        # Wait for 1 second before the next iteration
        sleep(1)


if __name__ == "__main__":
    main()
