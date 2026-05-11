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
        format_time = now_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(f"{file_name}", "w") as f:
            f.write(format_time)

        print(format_time, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
