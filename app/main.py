from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour:02}_{now.minute:02}_{now.second:02}.log"

        with open(filename, "w") as file:
            file.write(str(now))

        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
