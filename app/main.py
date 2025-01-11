from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = (f"app-{time_now.hour}_{time_now.minute}_"
                     f"{time_now.second}.log")
        try:
            with open(file_name, "w") as file:
                file.write(str(time_now))
        finally:
            file.close()
        print(f"{time_now} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
