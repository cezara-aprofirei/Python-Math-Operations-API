import asyncio
from math_service import MathService

math_service = MathService()

power_queue = asyncio.Queue()
fibonacci_queue = asyncio.Queue()
factorial_queue = asyncio.Queue()


async def power_worker():
    while True:
        base, exponent, future = await power_queue.get()
        try:
            result = math_service.power(base, exponent)
            future.set_result(result)
        except Exception as e:
            future.set_exception(e)
        power_queue.task_done()


async def fibonacci_worker():
    while True:
        n, future = await fibonacci_queue.get()
        try:
            result = math_service.fibonacci(n)
            future.set_result(result)
        except Exception as e:
            future.set_exception(e)
        fibonacci_queue.task_done()


async def factorial_worker():
    while True:
        n, future = await factorial_queue.get()
        try:
            result = math_service.factorial(n)
            future.set_result(result)
        except Exception as e:
            future.set_exception(e)
        factorial_queue.task_done()


async def start_workers():
    asyncio.create_task(power_worker())
    asyncio.create_task(fibonacci_worker())
    asyncio.create_task(factorial_worker())
