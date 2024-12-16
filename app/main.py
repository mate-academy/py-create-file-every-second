from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_data = datetime.now()
        file_name = (f"app-{current_data.hour}_"
                     f"{current_data.minute}_{current_data.second}.log")
        with open(file_name, "w") as file:
            file.write(str(current_data))
        print(current_data, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
