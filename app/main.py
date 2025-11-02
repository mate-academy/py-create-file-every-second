from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now().replace(microsecond=0)
        file_path = f"app-{now.hour}-{now.minute}_{now.second}.log"
        with open(file_path, "w") as f:
            f.write(f"{now}")
        print(str(now), file_path)
        time.sleep(1)


if __name__ == "__main__":
    main()
