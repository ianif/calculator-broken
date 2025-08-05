import time
from calculator import add, subtract, multiply, divide

start = time.time()
for _ in range(100000):
    add(1, 2)
    subtract(5, 3)
    multiply(3, 4)
    divide(10, 2)
end = time.time()

print(f"Benchmark completed in {end - start:.6f} seconds")

