import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_time = datetime.now()
        filename = (f"app-{current_time.hour}_"
                    f"{current_time.minute}_"
                    f"{current_time.second}.log")
        file_content = str(current_time)

        with open(filename, "w") as file:
            file.write(file_content)

        print(f"{file_content} {filename}")

        time.sleep(1)


if __name__ == "__main__":
    main()
