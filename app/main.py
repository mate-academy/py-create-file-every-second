from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now().date()
        time = datetime.now().strftime("%H:%M:%S")
        hour = datetime.now().hour
        minute = datetime.now().minute
        second = datetime.now().second
        file_name = f"app-{hour}_{minute}_{second}.log"
        with open(file_name, "w") as f:
            f.write(f"{date} {time}")
        print(f"{date} {time} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
