from datetime import datetime
from time import sleep


def main():
    while True:
        log_name = f"app-{datetime.now().strftime('%H_%M_%S')}.log"
        log_data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open(log_name, "w") as f:
            f.write(log_data)
        print(log_data, log_name)
        sleep(1)


if __name__ == "__main__":
    main()
