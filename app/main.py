import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        now = datetime.now()
        file_name = f"app-{now.strftime('%H_%M_%S')}.log"
        with open(file_name, "w") as f:
            f.write(f'{now}')
        print(now, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
