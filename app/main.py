import datetime
import time


def main():
    while True:
        t = datetime.datetime.now()
        name = t.strftime('app-%H_%M_%S.log')
        with open(name, 'w') as f:
            f.write(str(t))
            print(str(t), f.name)
            time.sleep(1)


if __name__ == "__main__":
    main()
