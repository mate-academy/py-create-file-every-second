from datetime import datetime
import time


def main():

    while True:
        now = datetime.now()
        hours = now.strftime("%H")
        minutes = now.strftime("%M")
        seconds = now.strftime("%S")
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(
                file_name,
                mode="w",
                newline="",
                encoding="utf-8"
        ) as file:
            file.write(timestamp)

        print(f"{timestamp} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
