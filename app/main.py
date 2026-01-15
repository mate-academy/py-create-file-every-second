from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        file_name = (f"app-{now.hour}_{now.minute}"
                     f"_{now.second}.log")
        content = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as f:
            f.write(content)
        time.sleep(1)
        print(content, file_name)


if __name__ == "__main__":
    main()
