from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second

        create_file = open(f"app-{hours}_{minutes}_{seconds}.log", "w")
        create_file.write(
            f"{now.year}-{now.month}-{now.day} "
            f"{hours}:{minutes}:{seconds}"
        )
        print(
            f"{now.year}-{now.month}-{now.day} "
            f"{hours}:{minutes}:{seconds} "
            f"app-{hours}_{minutes}_{seconds}.log"
        )
        create_file.close()

        time.sleep(1)


if __name__ == "__main__":
    main()
