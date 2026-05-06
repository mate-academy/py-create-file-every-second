import time

from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = str(datetime.now()).replace(" ", ".").split(".")
        hours, minutes, seconds = now[1].split(":")
        with open(f"app-{hours}_{minutes}_{seconds}.log", "a") as f:
            f.write(" ".join(now[:2]))
        print(" ".join(now[:2]) + f" app-{hours}_{minutes}_{seconds}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
