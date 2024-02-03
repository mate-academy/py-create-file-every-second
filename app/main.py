from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        file_content = str(current_time)
        with open(file_name, "w") as f:
            f.write(file_content)

        print(current_time, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
