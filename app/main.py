from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    # write your code here
    while True:
        c_time = datetime.now()
        file_name = (f"app-{c_time.hour}"
                     f"_{c_time.minute}"
                     f"_{c_time.second}.log")
        new_file = open(file_name, "w")
        new_file.write(str(c_time))
        print(datetime.now(), new_file.name)
        sleep(1)


if __name__ == "__main__":
    main()
