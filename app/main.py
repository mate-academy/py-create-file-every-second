import time


from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        new_file = open(f"app-{datetime.now().strftime('%H_%M_%S')}.log", "w")
        new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
              f"app-{datetime.now().strftime('%H_%M_%S')}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
