from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    file_name = input("Enter file name: ").strip()

    lines = []
    while True:
        line = input("Enter next line (type 'stop' to finish): ")
        if line.lower() == "stop":
            break
        lines.append(line)

    full_name = file_name + ".txt"

    with open(full_name, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
