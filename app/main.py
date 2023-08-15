from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        # Get the current date and time
        current_datetime = datetime.now()

        # Extract hours, minutes, and seconds
        hours = current_datetime.hour
        minutes = current_datetime.minute
        seconds = current_datetime.second

        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "w") as f:
            f.write(str(current_datetime))

        print(current_datetime, file_name)

        sleep(1)


if __name__ == "__main__":
    main()

print(datetime.now())
