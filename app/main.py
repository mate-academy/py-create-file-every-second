from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f'app-{now.strftime("%H_%M_%S")}.log'
        log = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as log_file:
            log_file.write(log)

        print(f"{log} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
