from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        file_name = f"app-{datetime.now().strftime('%H_%M_%S')}.log"
        with open(file_name, "w") as file:
            file.write(str(datetime.now()))
        print(datetime.now(), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
