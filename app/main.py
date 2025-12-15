from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        agora = datetime.now()
        year = agora.year
        month = agora.month
        day = agora.day
        hour = agora.hour
        minut = agora.minute
        sec = agora.second

        file_content = f"{year}-{month}-{day} {hour}:{minut}:{sec}"
        file_name = f"app-{hour}_{minut}_{sec}.log"

        with open(file_name, "w") as f:
            f.write(file_content)

        print(f"{file_content} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
