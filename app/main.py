from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        file_name = "app-" + str(
            datetime.now()
        ).split(" ")[1].replace(
            ":",
            "_"
        ) + ".log"
        with open(file_name, "w") as f:
            f.write(f"{datetime.now()}")
        print(f"{datetime.now()} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
