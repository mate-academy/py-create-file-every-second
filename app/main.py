import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now_time = str(datetime.now().time())
        file_name = f"app-{now_time[:2]}_{now_time[3:5]}_{now_time[6:8]}.log"
        with open(file_name, "w") as write_file:
            write_file.write(str(datetime.now()))
        print(f"{datetime.now()} {file_name}")
        write_file.close()
        time.sleep(1)


if __name__ == "__main__":
    main()
