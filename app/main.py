from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()

        time_formatted = time_now.strftime("%H_%M_%S")
        new_file_name = f"app-{time_formatted}.log"
        file_content = time_now.strftime("%Y-%m-%d %H:%M:%S")

        with open(new_file_name, "w") as f:
            f.write(file_content)
            f.close()

        print(f"{file_content} {new_file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
