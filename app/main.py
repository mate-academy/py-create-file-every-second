from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        data = datetime.now()
        file_name = f"app-{data.hour}_{data.minute}_{data.second}.log"
        file_content = (f"{data.year}-{data.month}-{data.day} {data.hour}:"
                        f"{data.minute}:{data.second}")
        with open(file_name, "w") as f:
            f.write(file_content)
        with open(file_name, "r") as f:
            print(f"{f.read()} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
