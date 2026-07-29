from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(file_name, "a") as file:
            time_str = "{}-{}-{} {}:{}:{}".format(now.year,
                                                  now.month,
                                                  now.day,
                                                  now.hour,
                                                  now.minute,
                                                  now.second
                                                  )
            file.write(time_str)

        with open(file_name, "r") as file:
            line = file.readline()
            print(line.strip(), file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
