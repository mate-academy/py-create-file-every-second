from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hour = now.hour
        minutes = now.minute
        seconds = now.second
        now = str(now)
        filename = f"app-{hour}_{minutes}_{seconds}.log"
        with open(filename, "w") as file:
            file.write(now)
        print(now, filename)
        sleep(1)


if __name__ == "__main__":
    main()
