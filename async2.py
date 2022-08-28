import asyncio

async def getPic(): #Proof of async def
    pic = 123
    return pic

async def main_def():
    print("A")
    print("Must await before get pic0...")
    pic0 = await asyncio.gather(getPic())
    print(pic0)
asyncio.run(main_def())