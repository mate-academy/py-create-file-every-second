from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        content = datetime.now()
        hours = content.strftime("%H")
        minutes = content.strftime("%M")
        seconds = content.strftime("%S")
        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "w") as f:
            f.write(str(content))

        print(content, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
