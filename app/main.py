from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()

        hour = now.hour
        minute = now.minute
        second = now.second

        name_archive = f"app-{hour}_{minute}_{second}.log"
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(name_archive, "w", encoding="utf-8") as arch:
            arch.write(timestamp)

        print(f"{timestamp} {name_archive}")

        time.sleep(1)


if __name__ == "__main__":
    main()
