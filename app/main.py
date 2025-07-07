from datetime import datetime
from time import sleep


def main() -> None:

    while True:
        now = datetime.now()

        filename = f"app-{now.strftime("%H_%M_%S")}.log"


        with open(filename, "w") as file:
            file.write(f"{now.strftime("%Y-%m-%d %H:%M:%S")}")


        print(f"{now.strftime("%Y-%m-%d %H:%M:%S")} {filename}", end="")

        sleep(1)
        print()


if __name__ == "__main__":
    main()
