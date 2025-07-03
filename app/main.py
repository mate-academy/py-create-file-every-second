from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()

        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        fin = open(file_name, "w")

        content = f"{now.date()} {now.time()}"
        fin.write(content)

        fin.close()

        print(f"{content} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
