from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        time_now = datetime.now()
        name_file = f"app-{time_now.hour}" \
                    f"_{time_now.minute}" \
                    f"_{time_now.second}.log"
        with open(name_file, "w") as f:
            f.write(str(time_now))

        print(time_now, name_file)
        sleep(1)


if __name__ == "__main__":
    main()
