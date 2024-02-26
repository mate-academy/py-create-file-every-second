import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> object:

    while True:
        tim = datetime.now()
        file_name = f"app-{tim.hour}_{tim.minute}_{tim.second}.log"
        with open(file_name, "w") as f:
            f.write(f"{tim}")
        time.sleep(1)
        print(f"{tim} {file_name}")


if __name__ == "__main__":
    main()
