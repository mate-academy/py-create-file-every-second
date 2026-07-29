from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> str:
    while True:
        hour = datetime.now()
        time.sleep(1)
        with open(
                f"app-{hour.hour}_{hour.minute}_{hour.second}.log", "w"
        ) as f:
            f.write(f"{hour}")
            print(f"{hour} app-{hour.hour}_{hour.minute}_{hour.second}.log")


if __name__ == "__main__":
    main()
