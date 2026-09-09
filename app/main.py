from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = str(datetime.now())
        file_name = f'app-{time.split()[1].replace(":", "_")}.log'
        with open(file_name, "w+") as f:
            f.write(time)
            print(f"{time} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
