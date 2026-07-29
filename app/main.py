from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    try:
        while True:
            saved_time = datetime.now()

            timestamp = saved_time.strftime("%Y-%m-%d %H:%M:%S")
            file_name = f"app-{saved_time.strftime('%H_%M_%S')}.log"

            with open(file_name, "w") as file:
                file.write(timestamp)

            print(f"{timestamp} {file_name}")

            sleep(1)

    except KeyboardInterrupt:
        raise
