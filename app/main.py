from datetime import datetime
import time
import sys

def main():
    # - File name must be in the following format:
    # `app-{hours}_{minutes}_{seconds}.log`.
    # - File content must be a timestamp of this
    # operation (example: 2007-06-29 13:49:40).
    # - The app must print to console timestamp and
    # newly created file name when it completes file
    # creation successfully.
    # - The app must run forever until you terminate
    # the process.
    while True:
        try:
            current_time = datetime.now()
            filename = f"app-{current_time.hour}_{current_time.minute}_{current_time.second}.log"
            timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

            with open(filename, "w") as file:
                file.write(timestamp)

            print(f"{timestamp} {filename}")
            sys.stdout.flush()
            time.sleep(1)

        except KeyboardInterrupt:
            raise
        except Exception as e:
            print(f"Error occurred: {e}", file=sys.stderr)
            sys.stderr.flush()


if __name__ == "__main__":
    main()
