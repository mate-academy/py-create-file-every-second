from datetime import datetime
from time import sleep


def main() -> None:
    try:
        while True:
            now = datetime.now()
            file_write = open(
                f"app-{now.hour}_{now.minute}_{now.second}.log", "w"
            )
            file_write.write(str(now.strftime("%Y-%m-%d %H:%M:%S")))
            print(
                f"{now.strftime('%Y-%m-%d %H:%M:%S')} "
                f"app-{now.hour}_{now.minute}_{now.second}.log"
            )
            file_write.close()
            sleep(1)
    except KeyboardInterrupt:
        raise KeyboardInterrupt


if __name__ == "__main__":
    main()
