from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        year, month, day, hour, minute, sec = (
            datetime.now().strftime("%Y %m %d %H %M %S").split()
        )
        filename = f"app-{hour}_{minute}_{sec}.log"
        filecontent = f"{year}-{month}-{day} {hour}:{minute}:{sec}"

        with open(filename, "w") as f:
            f.write(filecontent)
            print(f"{filecontent} {filename}")

        sleep(1)


if __name__ == "__main__":
    main()
