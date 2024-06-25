from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()

        file_name = f"app-{now.hour: 02}_{now.minute: 02}_{now.second: 02}.log"

        content = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(content)

        print(content, file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
