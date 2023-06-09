from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        created_file = (f"{now.year}-{now.month}-{now.day} "
                        f"{now.hour}:{now.minute}:{now.second}"
                        )
        with open(filename, "w") as f:
            f.write(created_file)
        print(created_file + " " + filename)
        sleep(1)


if __name__ == "__main__":
    main()
