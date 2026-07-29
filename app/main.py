from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.strftime('%H_%M_%S')}.log"
        content = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as file:
            file.write(content)

        print(f"{content} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
