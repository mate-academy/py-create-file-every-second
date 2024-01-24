import time
from datetime import datetime


def main() -> None:
    while True:
        try:
            formated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file_name = (f"app-{datetime.now().hour}_"
                         f"{datetime.now().minute}_"
                         f"{datetime.now().second}")
            with open(f"{file_name}.log", "w") as file:
                file.write(f"{formated_time}")
            print(f"{datetime.now()} {file_name}.log")
            time.sleep(1)
        except KeyboardInterrupt:
            raise
    pass


if __name__ == "__main__":
    main()
