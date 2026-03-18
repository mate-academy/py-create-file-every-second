from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        # Obtém data e hora atual
        now = datetime.now()

        # Formata nome do arquivo: app-hh_mm_ss.log
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # Formata conteúdo: YYYY-MM-DD HH:MM:SS
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        # Cria e escreve no arquivo
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(timestamp)

        # Imprime no console
        print(f"{timestamp} {file_name}")

        # Aguarda 1 segundo
        sleep(1)


if __name__ == "__main__":
    main()
