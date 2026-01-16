from datetime import datetime
from time import sleep


def main():
    while True:
        time = datetime.now()
        sleep(1)
        with open(f"app-{str(time)[11:13]}_{str(time)[14:16]}_"
                  f"{str(time)[17:19]}.log", "w") as f:
            f.write(str(time))
        print(time, f.name)


if __name__ == "__main__":
    main()
