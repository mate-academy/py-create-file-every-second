from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        time = datetime.now()
        new_name_to_file = f"app-{time.strftime('%H')}" \
                           f"_{time.strftime('%M')}" \
                           f"_{time.strftime('%S')}.log"

        with open(new_name_to_file, 'w') as file:
            file.write(f"{time}")
            sleep(1)
        print(time, new_name_to_file)


if __name__ == "__main__":
    main()
