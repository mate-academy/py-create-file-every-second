from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (f"app-{current_time.hour}"
                     f"_{current_time.minute}_"
                     f"{current_time.second}.log")
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(formatted_time)

        print(f"{formatted_time} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
