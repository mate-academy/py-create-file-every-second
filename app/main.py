from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_timestamp = datetime.now()
        hours = str(current_timestamp).split(":")[0].split(" ")[1]
        minutes = str(current_timestamp).split(":")[1]
        seconds = str(current_timestamp).split(":")[2].split(".")[0]
        filename = f"app-{hours}_{minutes}_{seconds}.log"

        with open(filename, "a") as file:
            file.write(str(current_timestamp))
        print(current_timestamp, filename)
        sleep(1)


if __name__ == "__main__":
    main()
