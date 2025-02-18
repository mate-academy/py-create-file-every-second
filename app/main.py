import asyncio
from datetime import datetime  # DO NOT CHANGE THIS IMPORT

async def main():
    while True:
        await asyncio.sleep(1)
        now = datetime.now()
        file_name =f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "w") as output_file:
            output_file.write(now.__str__().replace(":", "_") + f" {file_name}")
            print(f"{now.__str__()} {file_name}")
    
if __name__ == "__main__":
    asyncio.run(main())
