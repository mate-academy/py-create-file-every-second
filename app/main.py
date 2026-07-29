import time
from datetime import datetime


def main() -> None:
    while True:
        hour, minute, second = datetime.now().strftime("%H %M %S").split()
        file_name = f"app-{hour}_{minute}_{second}.log"
        with open(file_name, "w") as file:
            file.write(f"{datetime.now()}")
        print(datetime.now(), file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
