from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:

        just_now = datetime.now().replace(microsecond=0)

        filename = f"app-" \
                   f"{just_now.hour}_{just_now.minute}_{just_now.second}" \
                   f".log"

        with open(filename, "a") as f:
            f.write(f"{just_now}")

        print(f"{just_now} {filename}")

        sleep(1.0)


if __name__ == "__main__":
    main()
