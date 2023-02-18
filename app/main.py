import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        content = now.strftime("%Y-%m-%d %H:%M:%S")
        console_output = f"{content} {filename}"
        with open(f"{filename}", "w") as f:
            f.write(content)
            print(console_output)
        time.sleep(1)


if __name__ == "__main__":
    main()
