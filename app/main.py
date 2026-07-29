from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        content = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(f"{filename}", "w") as log_file:
            log_file.write(content)

        print(f"{content} {filename}")

        sleep(1)


if __name__ == "__main__":
    main()
