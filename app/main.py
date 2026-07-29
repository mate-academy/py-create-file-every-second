from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        data_time_now = str(now).split(".", 1)[0]
        hour = now.hour
        minute = now.minute
        second = now.second
        file_name = f"app-{hour}_{minute}_{second}.log"

        with open(file_name, "w") as d:
            d.write(data_time_now)
            print(data_time_now, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
