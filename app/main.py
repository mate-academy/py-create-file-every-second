from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        c_time = datetime.now()
        file_name = f"app-{c_time.hour}_{c_time.minute}_{c_time.second}.log"
        with open(file_name, "w") as file:
            file.write(c_time.isoformat(" ", "seconds"))
        print(c_time.isoformat(" ", "seconds"), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
