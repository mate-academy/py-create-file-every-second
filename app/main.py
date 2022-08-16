from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        t = datetime.now()
        h, m, s = t.hour, t.minute, t.second
        with open(f"app-{h}_{m}_{s}.log", "w") as f:
            f.write(str(t))
            print(t, f.name)
        sleep(1)


if __name__ == "__main__":
    main()
