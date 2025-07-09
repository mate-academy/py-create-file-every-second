from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        year, month, day, hour, minute, second = (
            datetime.now().strftime("%Y,%m,%d,%H,%M,%S").split(",")
        )
        filename = f"app-{hour}_{minute}_{second}.log"
        with (open(filename, "w") as file):
            string = (
                year + "-" + month + "-" + day
                + " " + hour + ":" + minute + ":" + second
            )
            file.write(string)
            print(
                string, filename)
        sleep(1)


if __name__ == "__main__":
    main()
