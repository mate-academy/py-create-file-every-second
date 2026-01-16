from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (f"app-{current_time.hour}"
                     f"_{current_time.minute}"
                     f"_{current_time.second}.log")
        with open(file_name, "w") as f:
            f.write(current_time.__str__())
            print(current_time.__str__(), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
