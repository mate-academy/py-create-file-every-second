from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        temp = datetime.now()
        filename = f"app-{temp.hour}_{temp.minute}_{temp.second}.log"
        with open(filename, "w") as writer:
            writer.write(f"{temp}")
        print(f"{temp} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
