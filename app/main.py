from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_datetime = datetime.now()
        name = current_datetime.strftime("app-%H_%M_%S.log")
        content = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        with open(name, "w") as file:
            file.write(content)
            print(f"{content} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
