from datetime import datetime
import time


def main():

    while 1:
        f_ = str(datetime.now())
        with open("app-" + f_[11:13] + "_" + f_[14:16] +
                  "_" + f_[17:19] + ".log", "w+") as f:
            f.write(str(datetime.now()))
            print((str(datetime.now()) + " app-" +
                   f_[11:13] + "_" + f_[14:16] + "_" + f_[17:19] + ".log"))
            time.sleep(1)


if __name__ == "__main__":
    main()
