from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> str:
    while True:
        now = datetime.now()
        now_name = now.strftime("%H_%M_%S")
        now_text = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(f"app-{now_name}.log", "w""") as f:
            f.write(now_text)

        print(now_text, f"app-{now_name}.log")
        time.sleep(1)
    # write your code here
    pass


if __name__ == "__main__":
    main()
