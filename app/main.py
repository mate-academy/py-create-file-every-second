from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        try:
            today = datetime.now()
            second = today.second
            minute = today.minute
            hour = today.hour
            file_name = f"app-{hour}_{minute}_{second}.log"
            timestamp = today.replace(microsecond=0)

            print(f"{timestamp} {file_name}")

            with open(f"{file_name}", "w") as file:
                file.write(f"{timestamp}")
            sleep(1)
        except KeyboardInterrupt:
            raise


if __name__ == "__main__":
    main()
