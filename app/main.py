from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now()
        file_name = f"app-{current_date.hour}_" \
                    f"{current_date.minute}_{current_date.second}.log"
        with open(file_name, "w") as file:
            file.write(str(current_date))
            print(str(current_date) + " " + file_name)
            sleep(1)


if __name__ == "__main__":
    main()
