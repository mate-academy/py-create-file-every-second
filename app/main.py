import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:

        this_time = datetime.now()
        current_time = str(this_time)
        with open(f"app-{this_time.hour}_{this_time.minute}_"
                  f"{this_time.second}.log", "w+") as file:
            file.write(f"{current_time}")
            file.seek(0)
            print(file.read(), file.name)
            time.sleep(1)


if __name__ == "__main__":
    main()
