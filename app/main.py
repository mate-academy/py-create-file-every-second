from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        filename = f"app-{hours}_{minutes}_{seconds}.log"

        # now_date = now.date()
        # now_time = now.time().replace(microsecond=0)

        file_content = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "a") as f:
            f.write(file_content)

        print(file_content + " " + filename)

        sleep(1)


if __name__ == "__main__":
    main()
