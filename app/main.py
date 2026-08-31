import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> str:

    while True:
        hour = datetime.now().hour
        minute = datetime.now().minute
        second = datetime.now().second

        file_name = f"app-{hour}_{minute}_{second}.log"
        file_content = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(f"{file_name}", "a") as file:
            file.write(file_content)
        print(file_content + " " + file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
