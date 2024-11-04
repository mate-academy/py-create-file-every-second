from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        dt = datetime.now()
        today = dt.strftime("%H_%M_%S")
        filename = f"app-{today}.log"
        content = dt.__str__()
        with open(filename, "w") as fp:
            fp.write(content)
        print(f"{content} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
