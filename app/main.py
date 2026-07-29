from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        c_time = datetime.now()
        file_name = f"app-{c_time.hour}_{c_time.minute}_{c_time.second}"
        file_name += ".log"
        with open(file_name, "w") as file:
            file.write(c_time.strftime("%Y-%m-%d %H:%M:%S"))
        file.close()
        print(f"{c_time} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
