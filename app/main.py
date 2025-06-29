from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        hour = datetime.now().hour
        minute = datetime.now().minute
        second = datetime.now().second
        formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{hour}_{minute}_{second}.log"
        with open(filename, "w") as f:
            f.write(formatted_time)
        print(f"{formatted_time} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
