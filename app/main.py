from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_name = datetime.now().strftime("app-%H_%M_%S.log")

        with open(file_name, "w") as file:
            file.write(current_time)

        print(current_time, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
