import time
from datetime import datetime


def main() -> None:
    while True:
        current_datatime = datetime.now()
        with open(
                f"app-{current_datatime.strftime('%H_%M_%S')}.log",
                "w"
        ) as f:
            f.write(f"{current_datatime}")
            print(
                f"{current_datatime} "
                f"app-{current_datatime.strftime('%H_%M_%S')}.log"
            )
        time.sleep(1)


if __name__ == "__main__":
    main()
