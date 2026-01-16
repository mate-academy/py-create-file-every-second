from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()

        file_name = (
            f"app-{current_time.hour}_"
            f"{current_time.minute}_{current_time.second}.log"
        )

        file_content = current_time.strftime("%Y-%m-%d %H:%M:%S")

        try:
            # Write the timestamp to the file
            with open(file_name, "w") as file:
                file.write(file_content)

            print(f"{file_content} {file_name}")

        except Exception as e:
            print(f"Error creating file {file_name}: {e}")

        sleep(1)


if __name__ == "__main__":
    main()
