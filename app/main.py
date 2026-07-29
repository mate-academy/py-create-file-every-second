from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        timestamp = datetime.now()
        file_name = timestamp.strftime("app-%H_%M_%S.log")
        file_content = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        with open(f"{file_name}", "w") as file:
            file.write(file_content)
            print(f"{file_content} {file_name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
