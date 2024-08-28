from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        hours, minutes, seconds = (
            datetime.now().hour,
            datetime.now().minute,
            datetime.now().second,
        )
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            f.write(str(datetime.now()))
            print(datetime.now(), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
