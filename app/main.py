from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:

        time_now = datetime.now()

        file_name = time_now.strftime("app-%H_%M_%S.log")
        file_content = str(time_now)
        print(file_content, file_name)

        with open(file_name, "w") as f:
            f.write(file_content)

        sleep(1)


if __name__ == "__main__":
    main()
