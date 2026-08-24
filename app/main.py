import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:

    while True:
        current_date = datetime.now()
        content_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
        file_name = (f"app-{current_date.hour}_"
                     f"{current_date.minute}_"
                     f"{current_date.second}.log")

        with open(f"{file_name}", "w") as file:
            file.write(content_date)

        print(f"{content_date} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
