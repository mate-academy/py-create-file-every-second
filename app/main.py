from datetime import datetime
import time


def main() -> None:

    while True:
        now = datetime.now()
        file_name = f"app-{now:%H_%M_%S}.log"
        file_content = f"{now:%Y-%m-%d %H:%M:%S}"
        with open(file_name, "w") as file:
            file.write(file_content)
            print(f"{file_content} {file_name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
