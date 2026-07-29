from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        app = datetime.now()
        full_name = app.strftime("app-%H_%M_%S.log")
        timestamp = app.strftime("%Y-%m-%d %H:%M:%S")

        with open(full_name, "w") as f:
            f.write(timestamp)
        print(f"{timestamp} {full_name}")

        sleep(1)


if __name__ == "__main__":
    main()
