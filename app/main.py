from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now().replace(microsecond=0)
        time = now.time()
        file_name = f"app-{time.hour}_{time.minute}_{time.second}.log"
        with open(file_name, "w") as file:
            file.write(str(now))
        print(f"{now} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
