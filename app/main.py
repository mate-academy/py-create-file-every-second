from datetime import datetime
import time


def main() -> None:
    while True:
        date = datetime.now()
        filename = f"app-{date.strftime("%H_%M_%S")}.log"
        with open(filename, mode="w") as file:
            file.write(f"{date}")
        print(f"{date.strftime("%Y-%m-%d %H:%M:%S")} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
