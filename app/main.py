from datetime import datetime
import time


def main() -> None:
    def callback() -> None:
        time_now = datetime.now()
        name = f"app-{time_now.strftime('%H_%M_%S')}.log"
        data = f"{time_now}"
        print(f"{data} {name}")

        with open(name, "a") as f:
            f.write(data)

    while True:
        callback()
        time.sleep(1)
    pass


if __name__ == "__main__":
    main()
