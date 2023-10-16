import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        temp_time = datetime.now()
        filename = (f"app-{temp_time.hour}_"
                    f"{temp_time.minute}_"
                    f"{temp_time.second}.log")

        with open(filename, "w") as file:
            file.write(f"{temp_time}")
            print(temp_time, filename)
            time.sleep(1)


if __name__ == "__main__":
    main()
