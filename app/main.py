from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_f = datetime.now()

        file_name = f"app-{time_f.strftime('%H_%M_%S')}.log"

        with open(file_name, "w") as fp:
            fp.write(str(time_f))

        print(f"{time_f} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
