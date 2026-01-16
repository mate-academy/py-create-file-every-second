# main.py

# Importa as bibliotecas necessárias para manipulação de data/hora e pausas.
# A diretriz do projeto especifica o uso de 'from datetime import datetime'.
from datetime import datetime
import time


def main() -> None:
    """
    Função principal que executa o ciclo de criação de ficheiros.
    """
    # Inicia o ciclo infinito para executar o programa continuamente.
    # A suite de testes espera que uma KeyboardInterrupt termine o programa,
    # por isso não a capturamos com um try/except.
    while True:
        # 1. Captura o timestamp atual uma única vez por iteração.
        current_time = datetime.now()

        # 2. Formata o timestamp para o conteúdo do ficheiro.
        file_content = current_time.strftime("%Y-%m-%d %H:%M:%S")

        # 3. Gera o nome do ficheiro.
        hour = current_time.hour
        minute = current_time.minute
        second = current_time.second
        file_name = f"app-{hour}_{minute}_{second}.log"

        # 4. Escreve o conteúdo no ficheiro usando um gestor de contexto.
        with open(file_name, "w") as f:
            f.write(file_content)

        # 5. Imprime a saída formatada na consola.
        print(f"{file_content} {file_name}")

        # 6. Pausa a execução por 1 segundo antes da próxima iteração.
        time.sleep(1)


if __name__ == "__main__":
    main()
