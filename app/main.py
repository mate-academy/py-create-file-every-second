import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        ctime = datetime.now()
        file_name = f"app-{ctime.hour}_{ctime.minute}_{ctime.second}.log"
        with open(file_name, "w") as f:
            f.write(str(ctime))
        print(f"{ctime} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
