from datetime import datetime
import time


def main():
    while True:
        current_time = datetime.now()
        file_name = current_time.strftime("app-%H_%M_%S.log")
        f = open(file_name, 'w')
        f.write(str(current_time))
        print(current_time, file_name)
        time.sleep(1)

if __name__ == "__main__":
    main()