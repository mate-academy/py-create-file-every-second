from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()

        file_name = f"app-{time_now.strftime('%H_%M_%S')}.log"
        text_for_file = time_now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w", encoding="utf-8") as f:
            f.write(text_for_file)

        print(f"{text_for_file} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
