from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now()
        filename = (f"app-"
                    f"{current_date.hour}_"
                    f"{current_date.minute}_"
                    f"{current_date.second}"
                    f".log"
                    )
        current_date = str(current_date).split(".")[0]
        with open(filename, "w") as f:
            f.write(str(current_date))
            print(f"{current_date} {filename}")

        sleep(1)


if __name__ == "__main__":
    main()
