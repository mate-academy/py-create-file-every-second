from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        hours = time.hour
        minutes = time.minute
        seconds = time.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            f.write(str(time))
        print(f"{time} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
