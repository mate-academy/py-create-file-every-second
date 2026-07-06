from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.strftime('%H_%M_%S')}.log"
        content = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as f:
            f.write(content)

        print(f"{content} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
