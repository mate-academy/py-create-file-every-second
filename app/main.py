from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        actually_text = (f"app-{current_time.hour}_"
                         f"{current_time.minute}_{current_time.second}.log")
        with open(actually_text, "w") as f:
            f.write(f"{current_time}")

        sleep(1)
        print(f"{current_time} {actually_text}")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
