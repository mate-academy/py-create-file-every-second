from datetime import datetime
from time import sleep
from typing import Tuple, Optional


def create_and_log_file() -> Tuple[bool, Optional[str], Optional[str]]:
    """
    Cria um arquivo com timestamp no nome e no conteúdo.
    Imprime o nome do arquivo e o timestamp no console.
    """
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

    try:
        with open(filename, "w") as f:
            f.write(timestamp)
        print(f"{timestamp} {filename}")
        return True, filename, timestamp
    except Exception as e:
        print(f"Erro ao criar o arquivo: {e}")
        return False, None, None


def main() -> None:
    """
    Executa a função de criação de arquivo a cada segundo, indefinidamente.
    """
    while True:
        create_and_log_file()
        sleep(1)


if __name__ == "__main__":
    main()
