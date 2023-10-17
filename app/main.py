import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        time.sleep(1)
        with open(f"app-{str(datetime.hour)}_{str(datetime.minute)}_{str(datetime.second)}", "w") as file:
            file.write(f"{str(datetime.year)}-{str(datetime.month)}-{str(datetime.day)} {str(datetime.hour)}:{str(datetime.minute)}:{str(datetime.second)}")
        print(f"{str(datetime.year)}-{str(datetime.month)}-{str(datetime.day)} {str(datetime.hour)}:{str(datetime.minute)}:{str(datetime.second)} app-app-{str(datetime.hour)}_{str(datetime.minute)}_{str(datetime.second)}")


if __name__ == "__main__":
    main()
