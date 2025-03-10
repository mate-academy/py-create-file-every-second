import time
from datetime import datetime


def main() -> None:
    try:
        while True:
            now = datetime.now()
            filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
            with open(filename, "w") as f:
                f.write(f"{now.replace(microsecond=0)}")
            print(f"{now.replace(microsecond=0)} {filename}")
            time.sleep(1)
    except KeyboardInterrupt:
        raise KeyboardInterrupt


if __name__ == "__main__":
    main()
