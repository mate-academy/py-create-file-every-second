from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        t1 = datetime.now()
        file_name = f"app-{t1.hour}_{t1.minute}_{t1.second}.log"
        with open(file_name, "w") as file:
            file.write(str(t1))
        time.sleep(1)
        print(t1, file_name)


if __name__ == "__main__":
    main()
