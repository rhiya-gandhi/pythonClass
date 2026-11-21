import asyncio
async def main():
    task = asyncio.create_task(fn2())
    print("one")
    await asyncio.sleep(2)
    print("two")
    print("five")
    

async def fn2():
    print("three")
    await asyncio.sleep(1)
    print("four")
    await asyncio.sleep(2)

asyncio.run (main())