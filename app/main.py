from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        ts = datetime.now()
        filename = f"app-{ts.hour}_{ts.minute}_{ts.second}.log"
        content = ts.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"{content} {filename}")

        from time import sleep

        sleep(1)


if __name__ == "__main__":
    main()
