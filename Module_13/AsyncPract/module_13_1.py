import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(5, 0, -1):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {6 - i} шар")
    print(f"Силач {name} закончил соревнования")

async def start_tournament():
    tasks = [asyncio.create_task(start_strongman('Pasha', 3)),
            asyncio.create_task(start_strongman('Denis', 4)),
            asyncio.create_task(start_strongman('Apollon', 5))]

    for task in tasks:
        await task

asyncio.run(start_tournament())
