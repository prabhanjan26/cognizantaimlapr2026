import asyncio
import time
async def create_time():
    while True:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(create_time())