from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hour = now.hour
        minutes = now.minute
        seconds = now.second
        file_name = f"app-{hour}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            print(f"{str(now)} {file_name}")
            f.write(f"{str(now)}")

        sleep(1)


if __name__ == "__main__":
    main()
