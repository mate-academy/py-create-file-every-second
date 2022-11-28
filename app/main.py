from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now().time()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "w") as file:
            text = datetime.now()
            file.write(f"{text}")
            print(text, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
