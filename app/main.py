import time
from datetime import datetime


def main() -> None:
    while True:
        date_now = str(datetime.now())
        name = (f'app-{datetime.now().strftime("%H")}'
                f'_{datetime.now().strftime("%M")}'
                f'_{datetime.now().strftime("%S")}.log')
        mes = f"{datetime.now()} {name}"
        with open(name, "a") as f:
            f.write(date_now)
            print(mes)
            time.sleep(1)


if __name__ == "__main__":
    main()
