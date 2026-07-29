import os
from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        formatted_now = now.strftime("%H_%M_%S")
        filename = f"app-{formatted_now}.log"
        filepath = os.path.join(os.getcwd(), filename)

        with open(filepath, "w") as file:
            file.write(str(now))

        print(f"{now} {filename}")

        time.sleep(1)


if __name__ == "__main__":
    main()
