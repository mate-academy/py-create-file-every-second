import time
from datetime import datetime


def main() -> None:
    try:
        while True:
            create_file()
            time.sleep(1)
    except KeyboardInterrupt:
        raise


def create_file() -> None:
    now = datetime.now()
    file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
    file_content = str(now)
    with open(file_name, "w") as file:
        file.write(file_content)
    print(f"{now} {file_name}")


if __name__ == "__main__":
    main()
