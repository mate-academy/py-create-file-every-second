from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        name_file = now.strftime("app-%H_%M_%S.log")

        with open(name_file, "w") as f:
            f.write(str(now))

        print(f"{now} {name_file}")

        time.sleep(1)


if __name__ == "__main__":
    main()
