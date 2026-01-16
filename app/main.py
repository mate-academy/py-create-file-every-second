import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:

        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        filename = (f"app-{current_time.hour}_{current_time.minute}_"
                    f"{current_time.second}.log")

        with open(filename, "w") as file:
            file.write(formatted_time)
            print(f"{formatted_time} {filename}")

        time.sleep(1)


if __name__ == "__main__":
    main()
