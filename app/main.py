from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        text = time.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{time.hour}_{time.minute}_{time.second}" + ".log"
        with open(file_name, "w") as f:
            f.write(text)
            print(f"{text} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
