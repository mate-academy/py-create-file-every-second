from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    try:
        while True:
            time = datetime.now()
            file_name = f"app-{time.hour}_{time.minute}_{time.second}.log"

            content = time.strftime("%Y-%m-%d %H:%M:%S")

            with open(file_name, "a") as file:
                file.write(content)

            print(f"{content} {file_name}")

            sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
