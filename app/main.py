from datetime import datetime
import time


def main() -> None:
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


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAplicação encerrada pelo usuário.")
