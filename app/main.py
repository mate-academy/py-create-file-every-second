from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    try:
        while True:
            current_time = datetime.now()
            filename = "app-" + current_time.strftime("%H_%M_%S") + ".log"

            with open(filename, "w") as file_out:
                file_out.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))

            with open(filename, "r") as f:
                print(f.read(), filename)

            sleep(1)

    except KeyboardInterrupt:
        raise KeyboardInterrupt("Exiting...")


if __name__ == "__main__":
    main()
