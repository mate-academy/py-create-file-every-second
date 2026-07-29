from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()

        hour = now.hour
        minute = now.minute
        second = now.second

        file_name = f"app-{hour}_{minute}_{second}.log"

        content = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(content)

        print(content, file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
