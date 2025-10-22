from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        now = datetime.now()
        filename =\
            f"app-{now.hour:02d}_{now.minute:02d}_{now.second:02d}.log"

        try:
            with open(filename, "w") as f:
                f.write(now.strftime("%Y-%m-%d %H:%M:%S"))
                print(now.strftime("%Y-%m-%d %H:%M:%S"), filename)
                sleep(1)
        except Exception as e:
            print("Error writing to file", e)


if __name__ == "__main__":
    main()
