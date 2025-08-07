from pydantic import BaseModel, Field


class PowerInput(BaseModel):
    base: int = Field(..., description="Base for power calculation")
    exponent: int = Field(..., description="Exponent for power calculation")


class FibonacciInput(BaseModel):
    number: int = Field(..., description="Number for Fibonacci calculation")


class FactorialInput(BaseModel):
    number: int = Field(..., description="Number for factorial calculation")
