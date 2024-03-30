from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    current_time = datetime.now()
    file_name = (f"app-{current_time.hour}_{current_time.minute}_"
                 f"{current_time.second}.log")
    file_content = str(current_time)

    while True:
        output_file = open(file_name, "w")
        output_file.write(file_content)

        print(f"{current_time} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
