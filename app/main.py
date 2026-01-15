from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        file_name = (f"app-"
                     f"{now.hour}_"
                     f"{now.minute}_"
                     f"{now.second}.log")
        content = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "a") as f:
            f.write(content)
        print(f"{content} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
