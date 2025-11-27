from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        filename = f"app-{date.strftime("%H_%M_%S")}.log"
        with open(filename, mode="w") as file:
            content = date.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{content}")
        print(f"{content} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
