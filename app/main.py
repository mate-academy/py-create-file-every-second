from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        date = now.strftime("%H_%M_%S")
        filename = f"app-{date}.log"

        log_file = open(filename, "w")
        log_file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " " + filename)
        log_file.close()
        sleep(1)


if __name__ == "__main__":
    main()
