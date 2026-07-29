import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        t_stamp = datetime.now()
        file_name = f"app-{t_stamp.hour}_{t_stamp.minute}_{t_stamp.second}.log"
        with open(file_name, "w") as f:
            f.write(str(t_stamp))

        print(f"{str(t_stamp)} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
