import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        file_name = now.strftime("app-%H_%M_%S.log")
        content = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as f:
            f.write(content)
        print(f"{content} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
