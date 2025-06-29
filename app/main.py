from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now()
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{now.strftime('%H_%M_%S')}.log"
        with open(filename, "a") as f:
            f.filename(timestamp_str)


if __name__ == "__main__":
    main()
