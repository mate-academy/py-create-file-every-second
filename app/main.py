from datetime import datetime
import time

def main() -> None:
    while True:
        now = datetime.now()
        name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(name, "r", encoding="utf-8") as f:
            print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {name}")

            time.sleep(1)


if __name__ == "__main__":
    main()
