import time
from datetime import datetime


def main() -> None:
    while True:
        time_now = datetime.now()
        time_stamp = time_now.strftime("%Y-%m-%d %H:%M:%S.%f")
        file_name = (f"app-{time_now.hour}_{time_now.minute}"
                     f"_{time_now.second}.log")

        with open(file_name, "w") as file:
            file.write(time_stamp)

        print(f"Created file {file_name} at {time_stamp}")
        time.sleep(1)


if __name__ == "__main__":
    main()
