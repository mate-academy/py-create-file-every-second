from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:

        this_time = datetime.now()
        timestamp = str(this_time)
        file_name = f"app-{this_time.strftime("%H_%M_%S")}.log"

        with open(file_name, "w") as f:
            f.write(timestamp)
        print(timestamp, file_name)

        sleep(1)


if __name__ == "__main__":
    main()
