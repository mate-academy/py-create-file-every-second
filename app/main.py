from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        name_of_file = \
            f"app-{now.strftime('%H')}_" \
            f"{now.strftime('%M')}_{now.strftime('%S')}.log"
        with open(name_of_file, "w") as f:
            f.write(f"{now.strftime('%Y')}-{now.strftime('%m')}-"
                    f"{now.strftime('%d')} {now.strftime('%H')}:"
                    f"{now.strftime('%M')}:{now.strftime('%S')}")
            sleep(1)
        with open(name_of_file, "r") as f:
            text = f.read()
        print(text, name_of_file)


if __name__ == "__main__":
    main()
