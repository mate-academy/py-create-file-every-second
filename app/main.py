from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        xtime = datetime.now()
        name = f'app-{xtime.strftime("%H")}_' \
               f'{xtime.strftime("%M")}_' \
               f'{xtime.strftime("%S")}.log'
        with open(name, "w")as f:
            f.write(str(xtime))
        print(f"{xtime} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
