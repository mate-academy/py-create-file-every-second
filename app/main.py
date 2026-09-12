from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now_datetime = datetime.now()
        file_name = f"app-{now_datetime.hour}_{now_datetime.minute}_" \
                    f"{now_datetime.second}.log"
        with open(file_name, "w") as f:
            print(f"{now_datetime} {file_name}")
            f.write(f"{now_datetime}")
        sleep(1)


if __name__ == "__main__":
    main()
