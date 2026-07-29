
from datetime import datetime
from time import sleep


class KeyboardInterrupt(Exception):
    pass


def main() -> None:
    try:
        while True:
            log_now = datetime.now()

            filename = f"app-{log_now.strftime('%H_%M_%S')}.log"
            formatted_now_log = log_now.strftime("%Y-%m-%d %H:%M:%S")
            with open(filename, "w") as log_file:
                log_file.write(formatted_now_log)
            print(formatted_now_log, filename)
            sleep(1)
    except KeyboardInterrupt:
        print("Program stopped")


if __name__ == "__main__":
    main()
