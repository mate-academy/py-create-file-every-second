from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        now = now.replace(microsecond=0)
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "w") as f:
            f.write(f"{str(now.date())} {str(now.time())}")
            print(f"{str(now.date())} {str(now.time())} {file_name}")
            sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
