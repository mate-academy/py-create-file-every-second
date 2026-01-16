import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        name = (f"app-{datetime.now().hour}_"
                f"{datetime.now().minute}_{datetime.now().second}.log")
        content = f"{datetime.now()}"
        text = (f"{datetime.now()} app-{datetime.now().hour}_"
                f"{datetime.now().minute}_{datetime.now().second}.log")
        with open(f"{name}", "w") as file:
            file.write(content)
        print(text)
        time.sleep(1)


if __name__ == "__main__":
    main()
