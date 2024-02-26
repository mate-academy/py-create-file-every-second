from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        current_time = datetime.now()
        file_name = f"app-{current_time.hour}_{current_time.minute}_{current_time.second}.log"
        file_content = str(current_time)

        with open(file_name, "w") as file:
            file.write(file_content)

        print(f"{current_time} {file_name}")
        sleep(1)

if __name__ == "__main__":
    main()
