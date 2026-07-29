from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    working_program = True

    while working_program:
        hour = datetime.now().hour
        minute = datetime.now().minute
        second = datetime.now().second
        file_name = f"app-{hour}_{minute}_{second}.log"
        with open(file_name, "w") as f:
            f.write(str(datetime.now()))
            print(f"{datetime.now()} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
