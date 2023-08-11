from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        file_name = f"app-{now.hour:02d}_{now.minute:02d}_{now.second:02d}.log"
        file_content = timestamp + "\n"
        with open(file_name, "w") as file:
            file.write(file_content)
        time.sleep(1)


if __name__ == "__main__":
    main()
