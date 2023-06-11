'''
• Asyncio
• 
'''

import asyncio


async def func1():
  await asyncio.sleep(5)
  return 'func1'


async def func2():
  await asyncio.sleep(5)
  return 'func2'


async def func3():
  await asyncio.sleep(5)
  return 'func3'


async def main():
  res = await asyncio.gather(
      func1(),
      func2(),
      func3(),
  )
  print(res)

asyncio.run(main())


print('-----------------------------------------------------------------------------------------------------------------------------------')
