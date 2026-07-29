from datetime import datetime
import time


def main() -> None:
    while True:
        try:
            now = datetime.now()
            filename = now.strftime("app-%H_%M_%S.log")
            content = now.strftime("%Y-%m-%d %H:%M:%S")
            with open(filename, "w") as file:
                file.write(content)
            print(f"{content} {filename}")
            time.sleep(1)
        except Exception as e:
            print(e)
            time.sleep(1)


if __name__ == "__main__":
    main()
