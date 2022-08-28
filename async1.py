# Example Python program that prints
# the status of a asyncio.Task before
# and after it is complete
import asyncio

# Define coroutine
async def br():
    for i in range(0, 12, 3):
        print(i)
        await asyncio.sleep(1)

async def cr():
    for i in range(0, 10, 2):
        print(i)
        await asyncio.sleep(1)


# A coroutine that will bootstrap a Task
async def main():
    tsk = asyncio.create_task(cr())
    tsk2 = asyncio.create_task(br())
     
     # Task is not done yet    
    print("Task done:%s"%tsk.done())
    print("Task2 done:%s"%tsk2.done())
    await tsk
    await tsk2

    # Task is done now
    print("Task done:%s"%tsk.done())
    print("Task2 done:%s"%tsk2.done())

# Run the coroutine main() in an asyncio event loop
l = asyncio.new_event_loop()    
asyncio.set_event_loop(l)
asyncio.run(main())