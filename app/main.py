from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep
import os


def main() -> None:  # Adicionei o tipo de retorno
    while True:
        now = datetime.now()

        # Nome inicial do arquivo
        base_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        file_name = base_name
        counter = 1

        # Se o arquivo já existir, cria com sufixo _1, _2, etc.
        while os.path.exists(file_name):
            file_name = f"{base_name[:-4]}_{counter}.log"
            counter += 1

        # Conteúdo do arquivo
        content = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"{content} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
