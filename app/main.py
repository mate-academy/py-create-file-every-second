from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now_time = datetime.now()
        file_created = (
            f"app-{now_time.hour}_{now_time.minute}_{now_time.second}.log"
        )
        print(f"{now_time} {file_created}")

        with open(file_created, "w") as f:
            f.write(str(now_time))
        sleep(1)


if __name__ == "__main__":
    main()
