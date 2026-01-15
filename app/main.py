from datetime import datetime  # DO NOT CHANGE THIS IMPORT

import time


def main() -> None:
    while True:
        localtime = datetime.now()
        filename = (f"app-{localtime.hour}_"
                    f"{localtime.minute}_"
                    f"{localtime.second}.log")
        document = open(filename, "w")
        document.write(str(localtime))
        print(f"{localtime} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
