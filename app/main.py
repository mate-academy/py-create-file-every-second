from datetime import datetime
from time import sleep  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        current_time = datetime.now()
        name = (f"app-{current_time.hour}_"
                f"{current_time.minute}_"
                f"{current_time.second}.log")
        with open(name, "w") as file:
            file.write(str(datetime.now()))
        print(str(datetime.now()), name)
        sleep(1)


if __name__ == "__main__":
    main()
