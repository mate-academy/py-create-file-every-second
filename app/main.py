from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        now = datetime.now()
        file_name = f'app-{now.hour}_{now.minute}_' \
                    f'{str(now)[-2:len(str(now))]}.log'
        with open(f"{file_name}", "a") as f:
            f.write(str(now))
        print(now, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
