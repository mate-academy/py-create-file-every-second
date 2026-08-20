from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(f"app-"
                  f"{current_time.split()[1][:2]}"
                  f"_"
                  f"{current_time.split()[1][3:5]}"
                  f"_"
                  f"{current_time.split()[1][6:]}"
                  f".log", "w") as file:
            file.write(current_time)
            print(current_time, file.name)
        time.sleep(1)


if __name__ == "__main__":
    main()
