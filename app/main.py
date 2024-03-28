from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now_time = datetime.now()
        file_name = (f"app-{now_time.hour}_"
                     f"{now_time.minute}_"
                     f"{now_time.second}.log")
        file_log = now_time
        sleep(1)
        with open(file_name, "w") as file:
            file.write(str(file_log))
            print(f"{file_log} {file_name}")


if __name__ == "__main__":
    main()
