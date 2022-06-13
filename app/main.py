from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        current_time = datetime.now()
        temp_filename = str(datetime.now().strftime("app-%H_%M_%S.log"))
        with open(temp_filename, "w") as file_in:
            file_in.write(str(current_time))
            print(str(current_time), temp_filename)
        sleep(1)


if __name__ == "__main__":
    main()
