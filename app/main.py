from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        file_name = "app-" + datetime.now().strftime("%H_%M_%S") + ".log"
        content = str(datetime.now())
        print(content, file_name)
        with open(file_name, "x") as file:
            file.write(content)
        time.sleep(1)


if __name__ == "__main__":
    main()
