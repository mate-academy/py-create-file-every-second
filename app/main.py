from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        file_name = str(datetime.now()).split()[-1].split(".")[0]
        file_name = file_name.replace(":", "_")
        file_name = "app-" + file_name + ".log"
        with open(file=file_name, mode="w") as f:
            temp = str(datetime.now())
            f.write(temp)
            f.close()
        print(temp, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
