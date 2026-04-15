from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        content = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as f:
            f.write(content)

        time.sleep(1)
        print(f"{content} {filename}")


if __name__ == "__main__":
    main()
