import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now().replace(microsecond=0)
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        content = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as f:
            f.write(content)

        print(f"{content} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
