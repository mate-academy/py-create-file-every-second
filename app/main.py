from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        content = datetime.now()
        name_file = "app-" + str(content.hour) + "_" \
                    + str(content.minute) + "_" + str(content.second) + ".log"
        with open(name_file, "w+") as f:
            f.write(str(content))
            print(datetime.now(), name_file)
        sleep(1)


if __name__ == "__main__":
    main()
