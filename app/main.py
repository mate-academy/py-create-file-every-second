from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        file_name = "app-" + now.strftime("%H_%M_%S") + ".log"
        content = now.strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)
        with open(file_name, "w") as f:
            f.write(content)
        with open(file_name, "r") as f:
            print(f"{f.read()} {file_name}")


if __name__ == "__main__":
    main()
