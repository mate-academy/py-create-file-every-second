from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    file_name = input("Enter file name: ").strip()

    lines = []
    while True:
        line = input("Enter next line (type 'stop' to finish): ")
        if line.lower() == "stop":
            break
        lines.append(line)

    # use datetime to avoid unused import error
    timestamp = datetime.now().isoformat()
    lines.insert(0, f"Created at: {timestamp}")

    full_name = file_name + ".txt"

    with open(full_name, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
