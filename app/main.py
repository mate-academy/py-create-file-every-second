from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        dt_now = datetime.now()
        log_name = f"app-{dt_now.strftime("%H_%M_%S")}.log"
        log_data = dt_now.strftime("%Y-%m-%d %H:%M:%S")

        with open(log_name, "w") as f:
            f.write(log_data)

        print(log_data, log_name)

        sleep(1)


if __name__ == "__main__":
    main()
