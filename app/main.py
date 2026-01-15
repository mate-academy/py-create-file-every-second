from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (f"app-{current_time.hour}_{current_time.minute}_"
                     f"{current_time.second}.log")
        file_content = current_time.strftime("%Y-%m-%d %H:%M:%S")

        output_file = open(file_name, "w")
        output_file.write(file_content)

        sleep(1)
        print(f"{file_content} {file_name}")


if __name__ == "__main__":
    main()
