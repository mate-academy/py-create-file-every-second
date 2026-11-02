from datetime import datetime
import time


def main():
    print("Iniciando a geração de arquivos de log a cada segundo. Pressione Ctrl+C para encerrar.")
    
    try:
        while True:
            # Obtém a data e hora atual
            agora = datetime.now()
            
            # Formatações exigidas
            # Nome do arquivo: app-{hours}_{minutes}_{seconds}.log
            nome_arquivo = f"app-{agora.hour}_{agora.minute}_{agora.second}.log"
            
            # Conteúdo do arquivo: 2007-06-29 13:49:40 (YYYY-MM-DD HH:MM:SS)
            conteudo_timestamp = agora.strftime("%Y-%m-%d %H:%M:%S")
            
            # Cria e escreve o arquivo no diretório de trabalho atual
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                f.write(conteudo_timestamp)
            
            # Imprime no console o carimbo de data/hora e o nome do arquivo recém-criado
            print(f"{conteudo_timestamp} {nome_arquivo}")
            
            # Aguarda 1 segundo antes da próxima iteração
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nAplicação encerrada pelo usuário.")


if __name__ == "__main__":
    main()
