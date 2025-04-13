from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    # write your code here
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{
            datetime.now().hour}_{
            datetime.now().minute}_{
            datetime.now().second}.log"
        with open(f"{filename}", "a") as file:
            file.write(f"{current_time}")
        print(f"{current_time} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
