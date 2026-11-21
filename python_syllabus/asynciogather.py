import asyncio,time
async def work (name,delay):
    await asyncio.sleep(delay)
    return name
async def using_gather():
    start = time.time()
    await asyncio.gather(work("A" , 2) , work("B",4),work("C",1))
    print(f"time taken by gather {time.time() - start:.1f}s") #time taken is measured by substracting the time of print from the time of funtion start 

asyncio.run(using_gather())