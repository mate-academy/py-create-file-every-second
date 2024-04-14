from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        datet = datetime.now()
        hour = datet.hour
        minut = datet.minute
        seconds = datet.second
        filename = f"app-{hour}_{minut}_{seconds}.log"
        with open(filename, "a") as f:
            f.write(f"{datet}")
        print(datet, filename)
        sleep(1)


if __name__ == "__main__":
    main()
