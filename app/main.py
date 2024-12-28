from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        try:
            current_time = datetime.now()
            hours = current_time.hour
            minutes = current_time.minute
            seconds = current_time.second
            file_name = f"app-{hours}_{minutes}_{seconds}.log"
            
            file = open(file_name, "w")
            file.write(str(current_time))
            file.close()
            
            print(current_time, file_name)
            
            sleep(1)
        except KeyboardInterrupt:
            print("----\nProcess terminated by user.")
            break
        # comment


if __name__ == "__main__":
    main()
