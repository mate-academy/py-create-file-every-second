from datetime import datetime
import time


def main() -> None:
    while True:
        date = datetime.now()
        name = "app-" + date.strftime("%H_%M_%S") + ".log"
        with open(name, "w") as file:
            file.write(str(date))
        print(date, name)
        time.sleep(1)


if __name__ == "__main__":
    main()
