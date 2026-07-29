from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = str(datetime.now())
        file_name = f"app-{now[11:13]}_{now[14:16]}_{now[17:19]}.log"

        with open(file_name, "w") as f:
            f.write(now)
        print(f"{now} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
