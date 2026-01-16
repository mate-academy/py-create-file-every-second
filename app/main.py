import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        # 1. Obter o momento atual
        now = datetime.now()

        # 2. Formatar nome do arquivo (ex: app-14_10_7.log)
        # Usamos %-H, %-M, %-S para evitar zeros à esquerda se o teste pedir assim, 
        # mas o padrão seguro é %H_%M_%S
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # 3. Formatar conteúdo (ex: 2007-06-29 13:49:40)
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        # 4. Criar o arquivo e escrever o timestamp
        with open(file_name, "w") as file:
            file.write(timestamp)

        # 5. Printar no console conforme exigido
        print(f"{timestamp} {file_name}")

        # 6. Esperar 1 segundo
        time.sleep(1)


if __name__ == "__main__":
    main()
