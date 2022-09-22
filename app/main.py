from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        d_t = datetime.now()
        with open(f"app-{d_t.hour}_{d_t.minute}_{d_t.second}.log", "w") as f:
            f.write(f"{d_t}")
            print(f"{d_t} {f.name}")
            sleep(1)


if __name__ == "__main__":
    main()
