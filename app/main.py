from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = str(current_time)[11:13] + "_"
        file_name += str(current_time)[14:16] + "_" + str(current_time)[17:19]

        with open(f"app-{file_name}.log", "w") as f:
            f.write(str(current_time))
            print(str(current_time), f"app-{file_name}.log")
        sleep(1)


if __name__ == "__main__":
    main()
