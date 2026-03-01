from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        string = (now.strftime("%Y-%m-%d %H:%M:%S"))
        name = f"app-{hours}_{minutes}_{seconds}.log"
        file_user = open(name, "a")
        file_user.write(string)
        file_user.close()
        print(f"{string} app-{hours}_{minutes}_{seconds}.log")
        sleep(1)


if __name__ == "__main__":
    main()
