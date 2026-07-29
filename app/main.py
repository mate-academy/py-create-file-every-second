import time
from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.strftime('%H_%M_%S')}.log"
        content = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{content} {file_name}")
        with open(file_name, "w") as f:
            f.write(content)
        time.sleep(1)


if __name__ == "__main__":
    main()
