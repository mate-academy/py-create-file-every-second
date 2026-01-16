from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        timenow = datetime.now()
        nhours = timenow.hour
        nminutes = timenow.minute
        nseconds = timenow.second
        fname = f"app-{nhours}_{nminutes}_{nseconds}.log"
        with open(fname, "w") as file_name:
            file_name.write(f"{str(timenow)}")
        print(timenow, fname)
        time.sleep(1)


if __name__ == "__main__":
    main()
