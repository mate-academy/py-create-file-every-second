from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}"
        with open(file_name + ".log", "w") as file:
            inside_date = now.strftime("%Y-%m-%d %H:%M:%S")
            file.write(inside_date)
            print(f"{inside_date} {file_name}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
