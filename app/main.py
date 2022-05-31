import datetime
from time import sleep


def main():
    while True:
        # current time (c_t)
        c_t = datetime.datetime.now()
        file = f"app-{c_t.strftime('%H')}_" \
               f"{c_t.strftime('%M')}_" \
               f"{c_t.strftime('%S')}.log"

        with open(file, "w") as f:
            f.write(str(c_t))

        print(c_t, file)
        sleep(1)


if __name__ == "__main__":
    main()
