from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        dt_n = datetime.now()
        file_name = f"app-{dt_n.hour}_{dt_n.minute}_{dt_n.second}.log"
        with open(file_name, "w") as f:
            f.write(str(dt_n))
        print(dt_n, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
