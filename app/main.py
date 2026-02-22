from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now_time = datetime.now()
        file_name = (
            f"app-{now_time.hour}_"
            f"{now_time.minute}_"
            f"{now_time.second}.log"
        )
        with open(file_name, "w") as file:
            file.write(str(now_time))
        print(f"{now_time} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
