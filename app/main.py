from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        with open(f"app-{datetime.now().hour}_"
                  f"{datetime.now().minute}_"
                  f"{datetime.now().second}.log", "w+") as f:
            content = f"{datetime.now()}"
            f.write(content)
            print(content + f" {f.name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
