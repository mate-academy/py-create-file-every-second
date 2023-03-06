from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        attr = datetime.now()
        hours = attr.strftime("%H")
        minutes = attr.strftime("%M")
        seconds = attr.strftime("%S")
        name_file = f"app-{hours}_{minutes}_{seconds}.log"
        open_file = open(name_file, "w")
        open_file.write(f"{attr}")
        open_file.close()
        with open(name_file, "r") as f:
            label = f.read() + " " + name_file
            print(label)
        time.sleep(1)


if __name__ == "__main__":
    main()
