from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        my_time = str(datetime.now()).split(".")
        prep_file = f'app-{my_time[0].split()[1]}.log'.replace(":", "_")
        with open(prep_file, "w") as file:
            file.write(f'{datetime.now()}')
        print(f'{datetime.now()} {prep_file}')
        sleep(1)


if __name__ == "__main__":
    main()
