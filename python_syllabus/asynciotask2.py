# Fire and forget, safely. 
# Write main() that starts a background task logger() 
# which prints "log 1", "log 2", "log 3" with 1 second between each, using create_task. 
# Main itself only does await asyncio.sleep(2) and then prints "main done". 
# How many log lines appear when you use asyncio.run(main())? Then fix the code so all three logs always appear 
# (hint: await task).
import asyncio
async def main ():
    task = asyncio.create_task(logger())
    await asyncio.sleep(2)
    print("main done")
    await task #await task means: "pause main here until this task is completely finished."

async def logger():
    print("log1")
    await asyncio.sleep(1)
    print("log2")
    await asyncio.sleep(1)
    print("log3")
    await asyncio.sleep(1)

asyncio.run(main())