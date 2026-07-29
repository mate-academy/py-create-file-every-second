from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        stamp = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = now.strftime("app-%H_%M_%S.log")

        try:
            with open(file_name, "w") as file:
                file.write(stamp)
        except Exception as e:
            print("Exception: ", e)
        else:
            print(stamp, file_name)
        finally:
            sleep(1)


if __name__ == "__main__":
    main()
