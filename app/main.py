from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        file_name = f"app-{datetime.now().strftime("%H_%M_%S")}.log"
        time_stamp = datetime.now()
        with open(file_name, "w") as log:
            log.write(str(time_stamp))
            print(f"{time_stamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
