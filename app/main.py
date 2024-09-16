import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        dt = datetime.now()
        file_name = f"app-{dt.hour}_{dt.minute}_{dt.second}.log"
        with open(file_name, "w") as f:
            f.write(str(dt))
            print(dt, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
