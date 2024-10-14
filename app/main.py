import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    seconds = 5
    while seconds:
        current_time = datetime.now()
        name_file = (f"app-{current_time.hour}_"
                     f"{current_time.minute}_"
                     f"{current_time.second}.log")
        with open(name_file, "w") as f:
            content = current_time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(content)
        print(content, name_file)
        time.sleep(1)
        seconds -= 1


if __name__ == "__main__":
    main()
