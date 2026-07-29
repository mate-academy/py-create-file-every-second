from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        fix_date = datetime.now()
        file_name = f"app-{fix_date.strftime('%H_%M_%S')}.log"
        print(f"{fix_date} {file_name}")
        with open(file_name, "w") as f:
            f.write(f"{fix_date}")
        time.sleep(1)


if __name__ == "__main__":
    main()
