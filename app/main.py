import asyncio
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


async def main() -> None:
    while True:
        await asyncio.sleep(1)
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "w") as output_file:
            line = f"{now.__str__().replace(":", "_")} {file_name}"
            output_file.write(line)

if __name__ == "__main__":
    asyncio.run(main())
