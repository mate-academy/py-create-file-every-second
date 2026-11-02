from datetime import datetime
import time


def main() -> None:
    print(
        "Iniciando a geração de arquivos de log a cada segundo. "
        "Pressione Ctrl+C para encerrar."
    )

    try:
        while True:
            agora = datetime.now()

            nome_arquivo = (
                f"app-{agora.hour}_{agora.minute}_{agora.second}.log"
            )

            conteudo_timestamp = agora.strftime("%Y-%m-%d %H:%M:%S")

            with open(nome_arquivo, "w", encoding="utf-8") as f:
                f.write(conteudo_timestamp)

            print(f"{conteudo_timestamp} {nome_arquivo}")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nAplicação encerrada pelo usuário.")


if __name__ == "__main__":
    main()
