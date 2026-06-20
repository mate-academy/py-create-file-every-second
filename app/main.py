from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        only_time = datetime.now().strftime("%H_%M_%S")

        name = f"app-{only_time}.log"
        with open(name, "w") as f:
            f.write(str(now))
        print(now + " " + name)
        sleep(1)


if __name__ == "__main__":
    main()
