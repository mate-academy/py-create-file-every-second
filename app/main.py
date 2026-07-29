from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        dtn = datetime.now()
        hours = dtn.strftime("%H")
        minutes = dtn.strftime("%M")
        seconds = dtn.strftime("%S")
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        with open(filename, "w") as f:
            f.write(f"{dtn}")
        print(f"{dtn} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
