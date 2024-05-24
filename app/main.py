import time
from datetime import datetime


def main() -> None:
    while True:
        hours, minutes, seconds = datetime.now().strftime("%H %M %S").split()
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            f.write(f"{datetime.now()}")
        print(f"{datetime.now()} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
