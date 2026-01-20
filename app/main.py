from datetime import datetime  # DO NOT CHANGE THIS IMPORT

from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        file_name = f"app-{time.hour}_{time.minute}_{time.second}.log"

        with open(file_name, "w") as file:
            file.write(timestamp)

        print(f"{timestamp} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
