from datetime import datetime
from time import sleep


def main() -> None:
    try:
        while True:
            current_time = datetime.now()
            file_name = (f"app-{current_time.hour}_{current_time.minute}_{current_time.second}.log")
            with open(file_name, "w") as file:
                file.write(str(current_time))
                print(f"{current_time} {file_name}")
                sleep(1)
    except Exception:
        pass


if __name__ == "__main__":
    main()
