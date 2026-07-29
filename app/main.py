from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        time = datetime.now()
        file_name = f"app-{time.hour}_{time.minute}_{time.second}.log"
        file_contents = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as f:
            f.write(file_contents)
        print(f"{file_contents} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
