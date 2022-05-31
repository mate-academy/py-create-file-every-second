import datetime
from time import sleep


def main():
    while True:
        # current time (c_t)
        c_t = datetime.datetime.now()
        file = f"app-{c_t.hour}_{c_t.minute}_{c_t.second}.log"

        with open(file, "w") as f:
            f.write(str(c_t))

        print(c_t, file)
        sleep(1)


if __name__ == "__main__":
    main()
