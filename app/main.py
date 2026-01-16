from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        t_now = datetime.now()
        file_name = f"app-{t_now.hour}_{t_now.minute}_{t_now.second}.log"

        with open(file_name, "w+") as file:
            file.write(str(datetime.now()))

        print(f"{t_now} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
