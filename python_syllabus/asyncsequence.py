import time, asyncio
async def work(name,delay):
    await asyncio.sleep(delay)
    return name
async def using_seq():
    start = time.time()
    await work("A",4)
    await work("B",2)
    await work("C",1)
    print(f"sequence of the work {time.time() - start:.1f}s")
asyncio.run(using_seq())