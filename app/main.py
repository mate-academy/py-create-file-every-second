from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        date = datetime.now()
        file_name = f"app-{date.hour}" \
                    f"_{date.minute}_" \
                    f"{date.second}.log"

        with open(file_name, "a") as d:
            d.write(str(date))
            print(str(date), file_name)
            time.sleep(1)


if __name__ == "__main__":
    main()
