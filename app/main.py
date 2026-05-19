from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second

        name = f"app-{hour}_{minute}_{second}.log"
        text = str(now)[0: 19]

        new_file = open(name, "w")
        new_file.write(text)
        new_file.close()

        print(text + " " + name)
        sleep(1)


if __name__ == "__main__":
    main()
