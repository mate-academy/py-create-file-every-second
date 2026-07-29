from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    last = None
    while True:
        now = datetime.now()
        current = now.second
        if current != last:
            last = current
            filename = (f"app-{now.hour}"
                        f"_{now.minute}"
                        f"_{now.second}.log")
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            with open(filename, "w") as file:
                file.write(timestamp)
            print(timestamp, filename)


if __name__ == "__main__":
    main()
