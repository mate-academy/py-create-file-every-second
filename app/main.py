from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        time_now_file = time_now.strftime("app-%H_%M_%S.log")
        time_now_content = time_now.strftime("%Y-%m-%d %H:%M:%S")
        with open(time_now_file, "w") as file:
            file.write(time_now_content)
        print(time_now_content, time_now_file)
        time.sleep(1)


if __name__ == "__main__":
    main()
