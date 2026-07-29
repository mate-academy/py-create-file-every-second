from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        content_time = now.strftime("%Y-%m-%d %H:%M:%S")
        name_file = now.strftime("app-%H_%M_%S.log")
        with open(name_file, "w", encoding="utf-8") as file:
            file.write(content_time)
        print(content_time, name_file)
        time.sleep(1)


if __name__ == "__main__":
    main()
