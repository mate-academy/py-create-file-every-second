from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = now.strftime("app-%H_%M_%S")
        new_file = open(f"{file_name}.log", "w")
        new_file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        new_file.close()
        print(f'{now.strftime("%Y-%m-%d %H:%M:%S")} {file_name}.log')
        sleep(1)


if __name__ == "__main__":
    main()
