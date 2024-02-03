from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    try:
        while True:
            file_name = (f"app-{datetime.now().hour}_{datetime.now().minute}_"
                         f"{datetime.now().second}.log")
            with open(file_name, "w") as f:
                timestamp = str(datetime.now())
                f.write(timestamp)
                print(timestamp, file_name)
            sleep(1)
    except KeyboardInterrupt:
        raise KeyboardInterrupt


if __name__ == "__main__":
    main()
