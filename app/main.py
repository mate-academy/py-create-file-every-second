from datetime import datetime
from time import sleep
from typing import Optional


def create_log_files(loop_limit: Optional[int] = None, output_dir: str = ".") -> None:
    """Create log files with a timestamp in an optional limited loop."""
    try:
        loop_count = 0
        while loop_limit is None or loop_count < loop_limit:
            # Get the current timestamp
            current_time = datetime.now()

            # Format the file name
            file_name = (
                f"{output_dir}/app-{current_time.hour}_"
                f"{current_time.minute}_"
                f"{current_time.second}.log"
            )

            # Write the timestamp into the file
            with open(file_name, "w") as file:
                file.write(str(current_time))

            # Print the timestamp and file name to the console
            print(f"{current_time} {file_name}")

            # Wait for 1 second
            sleep(1)
            loop_count += 1

    except KeyboardInterrupt:
        print("\nProcess terminated by user.")


def main():
    """Main entry point of the application."""
    create_log_files()


if __name__ == "__main__":
    main()
