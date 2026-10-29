import time
from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now()
        archive_text = now.strftime("%Y-%m-%d %H:%M:%S")
        archive_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(archive_name, "w") as file:
            file.write(archive_text)
        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {archive_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
