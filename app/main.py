from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        content = datetime.now()
        time_str = content.strftime("%H:%M:%S")
        hours, minutes, seconds = time_str.split(":")
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as new_file:
            new_file.write(str(content))

        print(f"{content} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
