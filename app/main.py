import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    now = datetime.now()
    file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
    while True:
        with open(file_name, "w") as f:
            f.write(str(now))
        print(now, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
