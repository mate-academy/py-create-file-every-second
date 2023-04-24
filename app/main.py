from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        file_name = "app-" + datetime.now().strftime("%H_%M_%S") + ".log"
        with open(file_name, "w") as f:
            f.write(str(datetime.now()))
        print(str(datetime.now()) + " " + file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
