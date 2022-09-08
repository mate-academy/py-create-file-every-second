from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


class ContexManager:
    def __init__(self, hour, minute, second, mode):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(f"app-{self.hour}_{self.minute}_{self.second}.log", self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


def main():
    while True:
        with ContexManager(datetime.now().hour,
                           datetime.now().minute,
                           datetime.now().second,
                           "w") as f:
            f.write(str(datetime.now()))
            g = f.name
        with open(g, "r") as w:
            print(w.read(), w.name)
        sleep(1)


if __name__ == "__main__":
    main()
