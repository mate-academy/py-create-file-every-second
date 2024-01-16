import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        filename = (
            f"app-{datetime.now().hour}_"
            f"{datetime.now().minute}_"
            f"{datetime.now().second}.log"
        )
        content = f"{datetime.now()}"
        with open(filename, "w") as f:
            f.write(content)
        print(content, filename)
        time.sleep(1.0)


if __name__ == "__main__":
    main()
