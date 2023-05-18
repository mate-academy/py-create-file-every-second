from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_content = str(now)
        file_name = "app-" + now.strftime("%H_%M_%S") + ".log"
        with open(file_name, "w") as f:
            f.write(file_content)
        sleep(1)
        print(file_content, file_name)


if __name__ == "__main__":
    main()
