from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = (
            f"app-"
            f"{time_now.hour}_"
            f"{time_now.minute}_"
            f"{time_now.second}.log"
        )
        content = time_now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as f:
            f.write(content)

        print(content + " " + file_name)

        sleep(1)


if __name__ == "__main__":
    main()
