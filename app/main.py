from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        with open(filename , "w") as f:
            file_content = now.strftime("%Y-%m-%d %H:%M:%S")
            f.write(file_content)
        sleep(1)
        print(f"{now} {filename}")


if __name__ == "__main__":
    main()
