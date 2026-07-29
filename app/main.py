from datetime import datetime
from time import sleep


def create_file() -> None:
    now = datetime.now().replace(microsecond=0)

    filename = f"app-{now.strftime('%H_%M_%S')}.log"

    content = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "w") as f:
        f.write(content)

    print(f"{content} {filename}")


def main() -> None:
    while True:
        create_file()
        sleep(1)


if __name__ == "__main__":
    main()
