from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        c_time = datetime.now()
        f_name = f"app-{c_time.hour}_{c_time.minute}_{c_time.second}.log"
        fl = open(f_name, "w+")
        fl.write(str(c_time))
        print(c_time, f_name)
        fl.close()
        sleep(1)


if __name__ == "__main__":
    main()
