from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        formatted_time = current_time.strftime("%H_%M_%S")
        log_filename = f"app-{formatted_time}.log"
        with open(log_filename, "w") as f:
            f.write(str(current_time))

        with open(log_filename, "r") as f:
            f_content = f.read()
            print(f"{str(f_content)} {log_filename}")
        sleep(1.0)


if __name__ == "__main__":
    main()
