from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        filename = current_time.strftime("app-%H_%M_%S.log")

        with open(filename, "w") as file:
            file.write(formatted_time)

        print(formatted_time, filename)

        time.sleep(1)


if __name__ == "__main__":
    main()
