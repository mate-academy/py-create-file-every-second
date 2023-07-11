import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        date = datetime.now()
        name_of_file = f"app-{date.hour}_{date.minute}_{int(date.second)}.log"

        new_file = open(name_of_file, "w")
        new_file.write(f"{date}")
        new_file.close()

        print(f"{date} {name_of_file}")

        time.sleep(1)


if __name__ == "__main__":
    main()
