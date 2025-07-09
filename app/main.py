import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        name = f"app-{hours}_{minutes}_{seconds}.log"
        content = f"{datetime.now().replace(microsecond=0)}"
        with open(f"{name}", "w") as file:
            file.write(content)
        print(content, name)
        time.sleep(1)


if __name__ == "__main__":
    main()
