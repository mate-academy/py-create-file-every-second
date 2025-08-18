from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now:%H_%M_%S}.log"

        with open(file_name, "w") as file:
            file.write(now.strftime("%Y-%m-%d %H:%M:%S"))

        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {file_name}")

        if not test_mode:
            sleep(1)


if __name__ == "__main__":
    main()
