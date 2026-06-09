from datetime import datetime, time  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        file_name = f"app-{datetime.now().hour}_{datetime.now().minute}_{datetime.now().second}.log"
        with open(file_name, "w") as f:
            content = str(datetime.now()).split(".")[0]
            print(content + " " + file_name)
            f.write(content)
            sleep(1)

if __name__ == "__main__":
    main()

