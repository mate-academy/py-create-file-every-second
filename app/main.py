from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time

def main():
    while True:
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second

        file_name = f"app-{hour}-{minute}-{second}.log"
        file_content = now.strftime("%Y-%m-%d %H:%M:%S")

        file = open(file_name, 'w')
        file.write(file_content)
        file.close()
        print(f"{file_content} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
