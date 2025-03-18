from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        fail_name = f"app-{time.hour}_{time.minute}_{time.second}.log"
        with open(fail_name, "w") as file:
            file.write(f"{time}")
        print(time, fail_name)
        sleep(1)


if __name__ == "__main__":
    main()
