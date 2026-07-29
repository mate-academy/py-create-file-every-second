from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()

        year = now.year
        month = now.month
        day = now.day

        hour = now.hour
        minute = now.minute
        second = now.second

        filename = f"app-{hour:02d}_{minute:02d}_{second:02d}.log"
        filecontent = f"{year}-{month:02d}-{day:02d} \
{hour:02d}:{minute:02d}:{second:02d}"

        with open(filename, "w") as file:
            file.write(filecontent)

        print(filecontent, filename)

        time.sleep(1)


if __name__ == "__main__":
    main()
