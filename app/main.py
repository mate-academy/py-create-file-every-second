from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        file_content = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as new_file:
            new_file.write(file_content)

        print(f"{file_content} {filename}")
        sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
