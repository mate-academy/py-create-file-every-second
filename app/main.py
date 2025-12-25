from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import os
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now()
        new_file_name = f"app-{current_date.hour}_" \
                        f"{current_date.minute}_{current_date.second}.log"
        new_file_path = os.path.join(os.getcwd(), new_file_name)

        with open(new_file_path, "w") as f:
            f.write(f"{current_date}")

        print(f"{current_date} {new_file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
