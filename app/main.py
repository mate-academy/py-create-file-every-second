from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        file_content = time_now.strftime("%Y-%m-%d %H:%M:%S")
        with open(
                f"app-{time_now.hour}_{time_now.minute}_"
                f"{time_now.second}.log", "w"
        ) as f:
            f.write(file_content)
            print(f"{file_content} "
                  f"app-{time_now.hour}_{time_now.minute}_"
                  f"{time_now.second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
