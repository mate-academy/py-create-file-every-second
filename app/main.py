from datetime import datetime
from time import sleep


def main():
    while True:
        now = datetime.now()
        h, m, s = now.strftime("%H:%M:%S").split(":")
        file_name = f"app-{h}_{m}_{s}.log"
        with open(file_name, "w") as f:
            f.write(str(now))

        print(now, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
