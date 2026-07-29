from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        file_name = now.strftime("app-%H_%M_%S.log")
        timer = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(timer)
        print(f"{timer} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
