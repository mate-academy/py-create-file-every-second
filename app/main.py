from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()

        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")

        file_name = now.strftime("app-%H_%M_%S.log")

        data = f"{current_date} {current_time}"

        with open(file_name, "w") as file:
            file.write(data)

            print(f"{data} {file_name}")

            sleep(1)


if __name__ == "__main__":
    main()
