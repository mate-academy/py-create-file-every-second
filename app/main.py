from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        current_time = datetime.now()
        name_of_file = f"app-" \
                       f"{current_time.hour}_" \
                       f"{current_time.minute}_" \
                       f"{current_time.second}" \
                       f".log"
        with open(name_of_file, "w") as f:
            f.write(str(current_time))
            print(current_time, name_of_file)
        time.sleep(1)


if __name__ == "__main__":
    main()
