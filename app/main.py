from datetime import datetime
from time import sleep


def main():

    # t = 0
    while True:
        date_now = datetime.now()
        # print(date_now)
        date_now = str(date_now).split(" ")
        # print(date_now)
        date_now = date_now[1]
        # print(date_now)
        name = f"app-{date_now[0:2]}_{date_now[3:5]}_{date_now[6:8]}.log"
        print(name)
        with open(name, "a") as file:
            file.write(f"{datetime.now} {name}")
        sleep(1)
        # t += 1


if __name__ == "__main__":
    main()
