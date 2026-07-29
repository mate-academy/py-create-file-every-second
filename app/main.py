from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()

        log = now.strftime("%Y-%m-%d %H:%M:%S")
        f_name = f"app-{now.strftime('%H_%M_%S')}.log"
        line = log + " " + f_name
        with open(f_name, "a") as f:
            f.write(log)
        print(line)
        sleep(1)


if __name__ == "__main__":
    main()
