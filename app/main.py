import time
from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now().replace(microsecond=0)
        hours = now.strftime("%H")
        minutes = now.strftime("%M")
        seconds = now.strftime("%S")
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        print(now, file_name)
        with open(file_name, "w") as f:
            f.write(str(now))
        time.sleep(1)


if __name__ == "__main__":
    main()
