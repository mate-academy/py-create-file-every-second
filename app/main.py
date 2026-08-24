from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        log = f"app-{now.hour}_{now.minute}_{now.second}.log"
        data = (
            f"{now.year}-{now.month}-{now.day} "
            f"{now.hour}:{now.minute}:{now.second}"
        )
        with open(log, "w") as f:
            f.write(data)
        print(f"{data} {log}")
        sleep(1)


if __name__ == "__main__":
    main()
