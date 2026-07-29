import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        file_new = open(file_name, "w")
        file_new.write(str(now))
        file_new.close()
        print(str(now), file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
