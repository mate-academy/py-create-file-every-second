from datetime import datetime
import time


def main() -> None:
    while True:
        app_time = datetime.now()
        file_name = (
            f"app-{app_time.hour}_"
            f"{app_time.minute}_"
            f"{app_time.second}.log"
        )

        with open(file_name, "w") as f:
            f.write(f"{app_time}")
            print(f"{app_time} {file_name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
