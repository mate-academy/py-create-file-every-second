from datetime import datetime
import time


def main() -> None:
    while True:
        content = datetime.now()
        name = content.strftime("%H_%M_%S")
        with open(f"app-{name}.log", "w") as new_file:
            new_file.write(f"{content}")
        print(content, f"app-{name}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
