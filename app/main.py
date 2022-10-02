from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    try:
        while True:
            timestamp = datetime.now()
            file_name = f"app-{timestamp.hour}_{timestamp.minute}" \
                        f"_{timestamp.second}.log"
            with open(file_name, "w") as f:
                f.write(timestamp.strftime("%Y-%m-%d %H:%M:%S"))
                time.sleep(1)
            if f.closed:
                print(timestamp.strftime("%Y-%m-%d %H:%M:%S"), file_name)
    except KeyboardInterrupt:
        raise
