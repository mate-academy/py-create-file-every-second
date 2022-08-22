import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    temp = True
    while temp:
        temp_name = [f"app-{datetime.now().strftime('%H_%M_%S')}.log"]
        temp_time = [f"{datetime.now()}"]
        with open(f"{temp_name[0]}", "w") as f:
            f.write(f"{temp_time[0]}")
        print(temp_time[0], temp_name[0])
        del temp_name[0]
        del temp_time[0]
        time.sleep(1)


if __name__ == "__main__":
    main()
