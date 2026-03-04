from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def get_name(date: str) -> str:
    name_first = date[11] + date[12]
    name_second = date[14] + date[15] if date[14] != 0 else date[15]
    name_third = date[17] + date[18] if date[17] != 0 else date[18]
    new_name = str(name_first) + "_" + str(name_second) + "_" + str(name_third)
    return "app-" + new_name


def main() -> None:
    while True:
        name = datetime.now()
        new_name = get_name(str(name)) + ".log"
        print(name, new_name)
        with open(new_name, "w") as f:
            f.write(str(name))
        sleep(1)


if __name__ == "__main__":
    main()
