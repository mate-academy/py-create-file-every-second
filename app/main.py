from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()

        # Format filename as before
        file_name = now.strftime("app-%H_%M_%S.log")

        # Updated to exclude microseconds
        content = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(content)

        print(f"{content} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
