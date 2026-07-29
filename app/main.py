import time
from datetime import datetime


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = current_time.strftime("%H_%M_%S")
        with open(f"app-{file_name}.log", "w") as f:
            f.write(f"{current_time}")
            time.sleep(1.0)
            print(f"{current_time}", f.name)


if __name__ == "__main__":
    main()
