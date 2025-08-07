class MathService:
    @staticmethod
    def power(base: int, exponent: int) -> int:
        return base ** exponent

    @staticmethod
    def fibonacci(n: int) -> int:
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers")
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    @staticmethod
    def factorial(n: int) -> int:
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
