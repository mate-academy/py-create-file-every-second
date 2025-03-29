from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        time_now = datetime.now()
        name_of_file = f"app-{datetime.now().strftime('%H_%M_%S')}.log"

        with open(name_of_file, 'w') as file:
            file.write(str(time_now))

        print(time_now, name_of_file)
        time.sleep(1)


if __name__ == "__main__":
    main()
