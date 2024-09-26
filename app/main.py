import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        dt_now = datetime.now()
        file_name = dt_now.strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as f:
            f.write(f"{dt_now}")
        print(dt_now, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
