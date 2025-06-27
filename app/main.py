import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    #try:
        while True:
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            filename = f"app-{now.strftime('%H_%M_%S')}.log"

            with open(filename, "w") as file:
                file.write(timestamp)

            print(f"{timestamp} {filename}")
            time.sleep(1)
    # except KeyboardInterrupt:
    #     print("\nProgram stopped by user")
    # except Exception as e:
    #     print(f"An error occured: {e}")

if __name__ == "__main__":
    main()
