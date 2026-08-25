from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        file_name = f"app-{time.strftime('%H_%M_%S')}.log"
        if not file_name:
            return None
        with open(file_name, "a") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S"))
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {f.name}")
            sleep(1)


if __name__ == "__main__":
    main()
