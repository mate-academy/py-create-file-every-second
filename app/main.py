from datetime import datetime
from time import sleep


def main() -> None:

    while True:
        # Data e hora atual
        now = datetime.now()

        # Timestamp para conteúdo
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        # Nome do arquivo
        file_name = now.strftime("app-%H_%M_%S.log")

        # Criar arquivo
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(timestamp)

        # Mostrar no console
        print(timestamp, file_name)

        # Espera 1 segundo
        sleep(1)


if __name__ == "__main__":
    main()
