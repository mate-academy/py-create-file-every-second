from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time.sleep(1)
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "w") as output_file:
            output_file.write(f"{now.__str__().replace(':', '_')} {file_name}")


if __name__ == "__main__":
    main()
