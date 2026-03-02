import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    # write your code here

    while True:
        moment = str(datetime.now())
        seconds = moment[17:19]
        minutes = moment[14:16]
        hours = moment[11:13]
        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        stream = open(file_name, "w")
        stream.write(moment)
        stream.close()
        print(f"{moment} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
