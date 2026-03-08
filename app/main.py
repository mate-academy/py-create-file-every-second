from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now().replace(microsecond=0)
        with open(f"app-{now.hour}_{now.minute}_{now.second}.log", "w") as f:
            f.write(f"{now}")
        print(now, f.name)
        time.sleep(1)


if __name__ == "__main__":
    main()
