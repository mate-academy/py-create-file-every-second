from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()

        filename = "app-{0:02d}_{1:02d}_{2:02d}.log".format(
            now.hour, now.minute, now.second
        )

        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as file:
            file.write(timestamp)

        print("{} {}".format(timestamp, filename))

        sleep(1)


if __name__ == "__main__":
    main()
