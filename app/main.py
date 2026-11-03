from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time

def main():
    while True:
        currentTime = datetime.now()

        content = currentTime.strftime("%Y-%m-%d %H:%M:%S")
        file_name = currentTime.strftime("app-%H_%M_%S.log")

        with open(file_name, 'w') as f:
            f.write(content)

        print(f"{content} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
