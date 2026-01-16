from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        with open("app-" + str(datetime.now().hour) + "_"
                  + str(datetime.now().minute) + "_"
                  + str(datetime.now().second) + ".log", "w") \
                as file:
            file.write(str(datetime.now()))
            print(datetime.now(), file.name)
            time.sleep(1)


print(datetime.now().minute)
if __name__ == "__main__":
    main()
