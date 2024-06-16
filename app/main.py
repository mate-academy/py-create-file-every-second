from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time



def main():
    while True:
        currnet_time = datetime.now()

        file_name = f"app-{currnet_time.hour}_{currnet_time.minute}_{currnet_time.second}.log"

        with open(file_name, 'w') as f:
            timestamp = currnet_time.strftime('%Y-%m-%d %H:%M:%S.%f')
            f.write(timestamp)

        print(f"{timestamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
