from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now().replace(microsecond=0)
        file_name = (
            f"app-{now.hour}_"
            f"{now.minute}_"
            f"{now.second}.log"
        )

        with open(file_name, "w") as f:
            f.write(str(now))
        print(f"{now} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
