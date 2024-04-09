import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        file_name = (f"app-{datetime.now().hour}_"
                     f"{datetime.now().minute}_{datetime.now().second}.log")
        with open(file_name, "w") as f:
            file_content = f"{datetime.now()}"
            f.write(file_content)
            print(file_content + " " + file_name)
            time.sleep(1)


if __name__ == "__main__":
    main()
