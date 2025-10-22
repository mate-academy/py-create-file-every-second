from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        content = now.strftime("%Y-%m-%d %H:%M:%S")
        content1 = now.strftime("%H_%M_%S")
        with open(f"app-{content1}.log", "w") as f:
            f.write(content)
            print(content + f" app-{content1}.log")
        sleep(1)


if __name__ == "__main__":
    main()
