from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        filename = current_time.strftime("app-%H_%M_%S.log")
        file_content = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as f:
            f.write(file_content)
        print(f"{file_content} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
