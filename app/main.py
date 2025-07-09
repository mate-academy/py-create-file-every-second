import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        time_now = datetime.now()
        format_name_file = (f"app-{time_now.hour}_{time_now.minute}"
                            f"_{time_now.second}.log")
        with open(format_name_file, "w") as write_file:
            print_format = time_now.strftime("%Y-%m-%d %H:%M:%S")
            write_file.write(f"{print_format}")
            print(f"{print_format} {format_name_file}")
            time.sleep(1)


if __name__ == "__main__":
    main()
