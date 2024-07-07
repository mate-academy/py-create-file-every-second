import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        name = f"app-{datetime.now().strftime('%H_%M_%S')}.log"
        content = f"{datetime.now()}"
        with open(
                name, "w"
        ) as log:
            log.write(content)
            print(f"{content} {name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
