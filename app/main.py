from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        hours, minutes, seconds = (
            str(datetime.now().time()).split(".")[0].split(":")
        )
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as logger:
            time_stamp = str(datetime.now()).split(".")[0]
            logger.write(time_stamp)
            print(time_stamp, file_name)
            sleep(1)


if __name__ == "__main__":
    main()
