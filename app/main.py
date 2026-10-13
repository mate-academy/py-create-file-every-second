from datetime import datetime
import time

def main() -> None:
    while True:
        now = datetime.now()

        h = now.hour
        m = now.minute
        s = now.second

        name_archive = f"app-{h}_{m}_{s}.log"
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(name_archive, "w", encoding="utf-8") as arch:
            arch.write(timestamp)

        print(f"{timestamp} {name_archive}")

        time.sleep(1)


if __name__ == "__main__":
    main()
