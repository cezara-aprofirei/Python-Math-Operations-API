import asyncio

from fastapi import APIRouter, HTTPException

from models import PowerInput, FibonacciInput, FactorialInput
from db import Database
from workers import power_queue, fibonacci_queue, factorial_queue

router = APIRouter()
db = Database()


@router.post("/power")
async def calculate_power(input_data: PowerInput):
    if input_data.base is None or input_data.exponent is None:
        raise HTTPException(
            status_code=400,
            detail="Both base and exponent are required"
        )

    future = asyncio.get_running_loop().create_future()
    await power_queue.put(
        (input_data.base, input_data.exponent, future)
    )
    result = await future

    await db.log_request(
        "power",
        f"base={input_data.base}, exponent={input_data.exponent}",
        str(result)
    )
    return {"result": result}


@router.post("/fibonacci")
async def calculate_fibonacci(input_data: FibonacciInput):
    if input_data.number is None:
        raise HTTPException(
            status_code=400,
            detail="Number is required"
        )

    future = asyncio.get_running_loop().create_future()
    await fibonacci_queue.put((input_data.number, future))

    try:
        result = await future
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    await db.log_request(
        "fibonacci",
        f"number={input_data.number}",
        str(result)
    )
    return {"result": result}


@router.post("/factorial")
async def calculate_factorial(input_data: FactorialInput):
    if input_data.number is None:
        raise HTTPException(
            status_code=400,
            detail="Number is required"
        )

    future = asyncio.get_running_loop().create_future()
    await factorial_queue.put((input_data.number, future))

    try:
        result = await future
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    await db.log_request(
        "factorial",
        f"number={input_data.number}",
        str(result)
    )
    return {"result": result}
