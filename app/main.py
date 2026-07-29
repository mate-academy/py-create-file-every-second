from datetime import datetime
import time


def main() -> None:
    """
    Runs an infinite loop that creates a new log file every second.

    The file name is based on the current time (app-H_M_S.log),
    and the file content is the full timestamp.
    """
    while True:
        # Ми прибрали блок try...except KeyboardInterrupt
        # Тепер помилка переривання не буде "зловлена" всередині функції
        now = datetime.now()

        file_name = (
            f"app-{now.hour}_{now.minute}_{now.second}.log"
        )

        timestamp_content = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as f:
            f.write(timestamp_content)

        print(f"{timestamp_content} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
