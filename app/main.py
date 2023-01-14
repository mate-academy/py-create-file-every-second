import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    # write your code here
    while True:
        filename = "app-" + datetime.now().strftime("%H_%M_%S") + ".log"
        with open(filename, "w") as f:
            f.write(str(datetime.now()))

        print(str(datetime.now()) + " " + filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
