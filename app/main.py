from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        cr_time = datetime.now()
        filename = f"app-{cr_time.hour}_{cr_time.minute}_{cr_time.second}.log"
        with open(filename, "w") as f:
            f.write(str(cr_time))
        print(f"{cr_time} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
