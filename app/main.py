from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.strftime('%H_%M_%S')}.log"
        with open(filename, "w") as file:
            file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
