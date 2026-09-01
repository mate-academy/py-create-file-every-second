from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        hour = now.strftime("%H:%M:%S")
        filename = "app-" + hour.replace(":", "_") + ".log"

        with open(filename, "w") as f:
            f.write(f"{date} {hour}")
        print(f"{date} {hour} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
