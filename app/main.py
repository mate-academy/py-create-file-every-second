from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_ins = datetime.now()
        file_name = f'app-{time_ins.time().strftime("%H_%M_%S")}.log'
        with open(file_name, "w") as f:
            f.write(str(time_ins))
        print(time_ins, end="")
        print("", file_name)
        sleep(1)


if __name__ == "__main__":
    main()
