from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        name_file = f"app-{time.hour}_{time.minute}_{time.second}.log"
        with open(name_file, "w") as file:
            result = f"{time.year}-{time.month}-{time.day} "
            result += "{}:{}:{}".format(time.hour, time.minute, time.second)
            file.write(result)

            print(result, name_file)
        sleep(1)


if __name__ == "__main__":
    main()
