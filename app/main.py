import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]

    dir_parts: list[str] = []
    file_name: str | None = None

    if "-d" in args and "-f" in args:
        d_idx = args.index("-d")
        f_idx = args.index("-f")
        if d_idx < f_idx:
            dir_parts = args[d_idx + 1:f_idx]
            file_name = args[f_idx + 1] if f_idx + 1 < len(args) else None
        else:
            file_name = args[f_idx + 1] if f_idx + 1 < len(args) else None
            dir_parts = args[d_idx + 1:]
    elif "-d" in args:
        d_idx = args.index("-d")
        dir_parts = args[d_idx + 1:]
    elif "-f" in args:
        f_idx = args.index("-f")
        file_name = args[f_idx + 1] if f_idx + 1 < len(args) else None

    target_dir = os.path.join(*dir_parts) if dir_parts else ""

    if target_dir:
        os.makedirs(target_dir, exist_ok=True)

    if file_name is not None:
        file_path = (
            os.path.join(target_dir, file_name)
            if target_dir
            else file_name
        )

        lines: list[str] = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"{timestamp}\n")
            for index, line in enumerate(lines, start=1):
                file.write(f"{index} {line}\n")
            file.write("\n")


if __name__ == "__main__":
    create_file()
