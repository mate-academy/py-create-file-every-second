from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        time = datetime.now().replace(microsecond=0)
        with open(
                f"app-{time.hour}-{time.minute}_{time.second}.log", "w"
        ) as f:
            f.write(f"{time}")


if __name__ == "__main__":
    main()
