from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        file_name = f"app-{hour}_{minute}_{second}.log"
        with open(file_name, "w") as f:
            f.write(now.strftime("%Y-%m-%d %H:%M:%S"))
            print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {file_name}")
            sleep(1)


if __name__ == "__main__":
    main()
