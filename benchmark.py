# Author: IOANNNA
import time
from calculator import add, subtract, multiply, divide

# Cache function references to avoid global lookups in the loop
local_add = add
local_subtract = subtract
local_multiply = multiply
local_divide = divide

# Use perf_counter for more precise timing
start = time.perf_counter()
for _ in range(100000):
    local_add(1, 2)
    local_subtract(5, 3)
    local_multiply(3, 4)
    local_divide(10, 2)
end = time.perf_counter()

print(f"Benchmark completed in {end - start:.6f} seconds")
