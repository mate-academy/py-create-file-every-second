from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        current_date = datetime.now()
        file_name = f"app-{current_date.hour}_{current_date.minute}_" \
                    f"{current_date.second}.log"
        with open(file_name, "w") as f:
            f.write(str(current_date))
            print(str(current_date), file_name)
            time.sleep(1)


if __name__ == "__main__":
    main()
