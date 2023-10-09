from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        date_now_first = datetime.now()
        date_now = str(date_now_first).split(" ")
        date_now = date_now[1]
        name = f"app-{date_now[0:2]}_{date_now[3:5]}_{date_now[6:8]}.log"
        with open(name, "w") as file:
            file.write(str(date_now_first))
        print(f"{date_now_first} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
