from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        # Usa os atributos numéricos para corresponder ao formato app-H_M_S.log
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(file_name, "w", encoding="utf-8") as f:
            f.write(timestamp)

        print(f"{timestamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
