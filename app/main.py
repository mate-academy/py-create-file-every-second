from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        content = str(datetime.now())
        with open(file_name, "w") as f:
            f.write(content)
        print(content, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
