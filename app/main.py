from datetime import datetime
import time


def main() -> None:
    while True:
        name = (f"app-{datetime.now().hour}_"
                f"{datetime.now().minute}_"
                f"{datetime.now().second}.log")
        text = str(datetime.now())
        with open(f"{name}", "w") as f:
            f.write(text)
        print(f"{text} {name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
