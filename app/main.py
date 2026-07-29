import time
from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now()
        file_name = now.strftime("app-%H_%M_%S.log")
        content = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as file:
            file.write(content)
        print(content, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
