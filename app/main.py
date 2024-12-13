from datetime import datetime
import time


def main() -> None:
    while True:
        current = datetime.now()
        timestamp = current.strftime("%Y-%m-%d %H:%M:%S")
        file_name = (f"app-{current.strftime("%H")}_"
                     f"{current.strftime("%M")}_"
                     f"{current.strftime("%S")}.log")
        with open(file_name, "x") as file:
            file.write(timestamp)
        print(timestamp, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
