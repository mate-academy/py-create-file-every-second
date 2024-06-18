from datetime import datetime
import time


def main() -> None:
    while True:
        file_name = (f"app-"
                     f"{datetime.now().hour}_"
                     f"{datetime.now().minute}_"
                     f"{datetime.now().second}.log")
        with open(file_name, "w") as file:
            file.write(str(datetime.now()))
        print(str(datetime.now()), file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
