from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        timestamp_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        file_name = current_time.strftime("app-%H_%M_%S.log")

        with open(file_name, "w") as file:
            file.write(timestamp_string)	

        print(f"{timestamp_string} {file_name}")
        time.sleep(1)
    

if __name__ == "__main__":
    main()
