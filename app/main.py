from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = f"app-{time_now.hour}_\
{time_now.minute}_{time_now.second}.log"
        with open(file_name, "w") as file:
            file.write(time_now.isoformat(" ", "seconds"))
        time_mark = time_now.isoformat(" ", "seconds")
        print(f"{time_mark} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
