from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> str:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as f_out:
            f_out.write(time_stamp)
        print(f"{time_stamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
