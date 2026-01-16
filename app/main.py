import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        content = str(now)

        with open(filename, "w") as f:
            f.write(content)

        print(f"{now} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
