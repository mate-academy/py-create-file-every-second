from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        current_time = datetime.now()
        name = f"app-{current_time.strftime('%H_%M_%S')}.log"

        with open(name, "w") as f:
            f.write(str(current_time))
        print(current_time, name)
        sleep(1)


if __name__ == "__main__":
    main()
