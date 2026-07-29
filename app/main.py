from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        time = now.strftime("%H:%M:%S").split(":")
        file_name = f"app-{time[0]}_{time[1]}_{time[2]}.log"
        with open(file_name, "a") as file:
            file.write(f"{now}")
            print(f"{now} {file_name}")
            sleep(1)


if __name__ == "__main__":
    main()
