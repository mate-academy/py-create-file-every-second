from datetime import datetime
from time import sleep


def main() -> None:
    try:
        while True:
            current_time_stamp = datetime.now()

            name = (f"app-{current_time_stamp.hour}_"
                    f"{current_time_stamp.minute}_"
                    f"{current_time_stamp.second}.log")

            with open(name, "w") as file:
                file.write(current_time_stamp.strftime("%Y-%m-%d %H:%M:%S"))
            print(current_time_stamp, name)
            sleep(1)
    except KeyboardInterrupt:
        raise KeyboardInterrupt


if __name__ == "__main__":
    main()
