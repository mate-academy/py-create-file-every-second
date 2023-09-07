from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    all_times = ""
    while True:
        current_time = datetime.now()
        file_name = f"app-{current_time.strftime('%H_%M_%S')}.log"
        with open(file_name, "w") as file:
            file.write(str(current_time))
            all_times += f"{current_time} {file_name} "
            sleep(1)
        print(all_times)


if __name__ == "__main__":
    main()
