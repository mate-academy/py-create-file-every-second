import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        time_w = str(datetime.now())
        time_name = time_w[10:].split(":")
        time_name = "_".join(time_name)

        with open(f"app-{time_name[1:]}.log", "w") as filik:
            filik.write(time_w)
            print(time_w, filik.name)
            time.sleep(1)


if __name__ == "__main__":
    main()
