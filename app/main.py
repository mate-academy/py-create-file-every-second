from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        filename = (
            f"app-{current_time.hour}"
            f"_{current_time.minute}_"
            f"{current_time.second}.log"
        )

        with open(filename, "w") as f:
            f.write(str(current_time))

        print(f"{current_time} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
