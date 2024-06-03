from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        cur_time = datetime.now()
        file_name = (f"app-{cur_time.hour}_{cur_time.minute}_"
                     f"{cur_time.second}.log")
        with open(file_name, "w") as file:
            file.write(str(cur_time))
            print(f"{str(cur_time)} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
