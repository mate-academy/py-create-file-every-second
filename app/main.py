from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        name_file =\
            "app-" + str(datetime.now())[11:19].replace(":", "_") + ".log"
        with open(name_file, "w") as f:
            f.write(str(datetime.now()))
        print(f"{datetime.now()} {name_file}")
        sleep(1)


if __name__ == "__main__":
    main()
