from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = (f"app-{time_now.hour}_"
                     f"{time_now.minute}_{time_now.second}.log")
        file_data = str(time_now)

        with open(file_name, "w") as f:
            f.write(file_data)

        print(f"{file_data} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
