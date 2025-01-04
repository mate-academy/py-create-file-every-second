from datetime import datetime
import time


def main() -> None:
    try:
        while True:
            # Get the current timestamp
            current_time = datetime.now()
            # Format the filename as specified
            filename = (f"app-{current_time.hour}_{current_time.minute}_"
                        f"{current_time.second}.log")
            # Create and write to the file
            with open(filename, "w") as file:
                file.write(f"{current_time}")
            # Print the console message
            print(f"{current_time} {filename}")
            # Sleep for 1 second
            time.sleep(1)
    except KeyboardInterrupt:
        print("Process terminated.")


if __name__ == "__main__":
    main()
