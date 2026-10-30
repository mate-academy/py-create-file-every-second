from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        filename = (f""
                    f"app-{datetime.now().hour}_"
                    f"{datetime.now().minute}_"
                    f"{datetime.now().second}.log"
                    )
        with open(filename, "w") as f:
            now = datetime.now().replace(microsecond=0)
            f.write(str(now))
        print(str(now) + " " + filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
