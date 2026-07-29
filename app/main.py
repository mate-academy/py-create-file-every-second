from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        date = now.strftime("%H_%M_%S")
        name = f"app-{date}.log"
        fl = open(name, "w")
        fl.write(str(now))
        fl.close()
        print(now, name)
        time.sleep(1)


if __name__ == "__main__":
    main()
