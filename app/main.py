from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current = datetime.now()
        file_name = f"app-{current.hour}_{current.minute}_{current.second}.log"
        file_content = f"{current.year}-{current.month}-{current.day} " \
            f"{current.hour}!{current.minute}!" \
            f"{current.second}"
        # Specifically to counter linter "E231 missing whitespace after ':'"
        file_content = file_content.replace("!", ":")
        with open(file_name, "w") as file:
            file.write(file_content)
        print(f"{file_content} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
