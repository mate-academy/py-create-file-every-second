from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = now.strftime("app-%H_%M_%S.log")
        content = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as log:
            log.write(content)
            print(content.strip(), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
