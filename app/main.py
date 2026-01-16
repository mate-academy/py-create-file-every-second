from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        name_time = datetime.now().strftime("%H_%M_%S")
        file_name = f"app-{name_time}.log"
        file_content = str(datetime.now())

        with open(file_name, "w") as f:
            f.write(file_content)

        print(file_content, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
