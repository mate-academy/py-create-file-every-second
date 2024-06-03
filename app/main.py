from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        real_time = datetime.now()
        name = (f"app-{real_time.hour}_"
                f"{real_time.minute}_{real_time.second}.log")
        times = real_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(name, "w") as f:
            f.write(times)
        print(f"{times} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
