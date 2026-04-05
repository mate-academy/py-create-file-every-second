from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> str:
    while True:
        now = datetime.now()
        name_file = f"app-{now.hour}_{now.minute}_{now.second}.log"
        content = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(name_file, "w") as f:
            f.write(content)
        print(content + " " + name_file)
        time.sleep(1)


if __name__ == "__main__":
    main()
