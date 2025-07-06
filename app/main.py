from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        filename = (f"app-{current_time.hour}"
                    f"_{current_time.minute}"
                    f"_{current_time.second}.log")
        with open(filename, "w") as file:
            file.write(str(current_time))
        print(f"{current_time} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
