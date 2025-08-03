from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        file_name = "app-" + datetime.now().strftime("%H_%M_%S") + ".log"
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as file:
            file.write(f"{date_now}")
            print(date_now, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
