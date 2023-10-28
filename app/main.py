from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        data = datetime.now()
        file_name = f"app-{data.hour}_{data.minute}_{data.second}.log"
        with open(file_name, "w") as file:
            file.write(str(data))
        print(str(data), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
