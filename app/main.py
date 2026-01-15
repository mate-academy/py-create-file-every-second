import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_dt = datetime.now()
        new_file = open("app-" + str(current_dt.hour)
                        + "_" + str(current_dt.minute) + "_"
                        + str(current_dt.second) + ".log", "w")
        new_file.write(str(current_dt))
        new_file.close()
        print(str(current_dt) + " " + new_file.name)
        time.sleep(1)


if __name__ == "__main__":
    main()
