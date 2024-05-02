from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        time_formatted = current_time.strftime("%H_%M_%S")
        file_name = f"app-{time_formatted}.log"

        with open(file_name, "w") as f:
            f.write(f"{current_time}")
            print(f"{current_time} {file_name}")
            sleep(1)


if __name__ == "__main__":
    main()
