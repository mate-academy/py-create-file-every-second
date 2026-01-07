from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    # write your code here
    while True:
        current_time = datetime.now()
        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(filename, "w") as file:
                file.write(timestamp_str)
            print(timestamp_str, filename)
        except KeyboardInterrupt:
            break
        sleep(1)


if __name__ == "__main__":
    main()
