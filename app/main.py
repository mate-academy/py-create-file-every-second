from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = f'app-{time_now.strftime("%H_%M_%S")}.log'
        log_line = f'{time_now.strftime("%Y-%m-%d %H:%M:%S")}'
        with open(file_name, "w") as f:
            f.write(log_line)
        print(log_line + " " + file_name)
        sleep(1)


if __name__ == "__main__":
    main()
