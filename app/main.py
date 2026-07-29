from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        dt_now = datetime.now()
        file_name = f"app-{dt_now.hour}_{dt_now.minute}_{dt_now.second}.log"
        file_write = dt_now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as log:
            log.write(file_write)
        print(file_write, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
