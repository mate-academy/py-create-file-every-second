from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep

def main():
    now = datetime.now()
    file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

    while True:
        with open(file_name, "w") as f:
            f.write(str(now))

        print(str(now) + file_name)
        sleep(1)


if __name__ == "__main__":
    main()
