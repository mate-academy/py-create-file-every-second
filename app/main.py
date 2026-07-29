import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        mig = datetime.now()
        file_name = f"app-{mig.hour}_{mig.minute}_{mig.second}.log"

        with open(file_name, "w") as file:
            file.write(str(datetime.now()))
        with open(file_name, "r") as file:
            print(file.read(), file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
