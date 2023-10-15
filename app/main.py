from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time



def main() -> None:
    while True:
        current_date = datetime.now()
        file_name = current_date.strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as file:
            current_time = datetime.now()
            log_name = current_time.strftime("%Y-%m-%d %H:%M:%S")
            file.write(log_name)
            print(log_name, file_name)
            time.sleep(1)


if __name__ == "__main__":
    main()
