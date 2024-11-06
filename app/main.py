from datetime import datetime
import time


def create_files(num_files: int = 3) -> None:
    generated_files = 0

    while True:
        now = datetime.now()
        file_name = now.strftime("app-%H_%M_%S.log")
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(timestamp)

        print(f"{timestamp} {file_name}")

        generated_files += 1
        if generated_files >= num_files:
            raise KeyboardInterrupt

        time.sleep(1)


def main() -> None:
    create_files()


if __name__ == "__main__":
    main()
