from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        full_date = datetime.now()
        filename = (
            f"app-{full_date.hour}_"
            f"{full_date.minute}_"
            f"{full_date.second}.log"
        )
        content = (str(full_date))[:19]
        print(content, filename)
        sleep(1)

        with open(filename, "w") as f:
            f.write(content)


if __name__ == "__main__":
    main()
