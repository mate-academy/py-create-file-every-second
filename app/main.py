from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    """
    Crea un archivo de log cada segundo.
    Se eliminó el mensaje inicial para cumplir con las expectativas del test.
    """
    while True:
        # 1. Obtener el tiempo actual
        now = datetime.now()

        # 2. Formatear el contenido (Timestamp completo)
        timestamp_content = now.strftime("%Y-%m-%d %H:%M:%S")

        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # 4. Crear y escribir el archivo
        with open(file_name, mode="w", encoding="utf-8") as f:
            f.write(timestamp_content)

        # 5. Imprimir exactamente lo que el test espera
        print(f"{timestamp_content} {file_name}")

        # 6. Esperar 1 segundo
        time.sleep(1)


if __name__ == "__main__":
    main()
