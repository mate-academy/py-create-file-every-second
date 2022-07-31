from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        time_ = ((str(datetime.now().time()))[0:8]).replace(':', '_')
        name = "app-" + time_ + '.log'
        with open(name, "w+") as f:
            f.write(str(datetime.now()))
        with open(name, "r") as f:
            print(f.read() + ' ' + name)
        time.sleep(1)


if __name__ == "__main__":
    main()
