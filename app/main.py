from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        # 1. Get current time for content and filename
        now = datetime.now()

        # Format for file content: 2007-06-29 13:49:40
        content_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        # Format for filename: app-14_10_7.log
        # %-H, %-M, %-S (or %H, %M, %S) for hours, minutes, seconds
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # 2. Create the file and write the timestamp
        try:
            with open(filename, "w") as f:
                f.write(content_timestamp)

            # 3. Print success message to console
            print(f"{content_timestamp} {filename}")

        except Exception as e:
            print(f"Failed to create file {filename}: {e}")

        # 4. Wait for 1 second before the next iteration
        time.sleep(1)

if __name__ == "__main__":
    main()
