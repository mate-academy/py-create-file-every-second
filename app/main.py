from datetime import datetime
import time


def main() -> None:

    while True:

        content = str(datetime.now())
        hours, minutes, seconds = content.split(" ")[1].split(":")
        filename = f"app-{hours}_{minutes}_{seconds.split('.')[0]}.log"

        with open(filename, "w") as file:
            file.write(content)

        print(f"{content} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
