from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = (f"app-{now.strftime('%H')}"
                     f"_{now.strftime('%M')}"
                     f"_{now.strftime('%S')}.log")
        with open(file_name, "w") as file_time:
            file_time.write(f"{time}")
        print(f"{time} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
