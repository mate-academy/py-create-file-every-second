from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        content = datetime.now()
        file_name = f"app-{content.hour}_{content.minute}_{content.second}.log"
        with open(file_name, "a") as f:
            f.write(str(content))
        print(f"{content} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
