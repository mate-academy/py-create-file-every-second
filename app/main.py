from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = f"app-{current_time.strftime('%H_%M_%S')}.log"
        with open(file_name, "a") as f:
            f.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))
        print(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
