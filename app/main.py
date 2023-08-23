from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        ts = datetime.now()
        file_name = f"app-{ts.hour}_{ts.minute}_{ts.second}.log"
        with open(file_name, "w") as file:
            file.write(str(ts))
        print(str(ts) + " " + file_name)
        sleep(1)


if __name__ == "__main__":
    main()
