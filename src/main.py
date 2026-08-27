from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Rahaman Shifat")
print("Today's Date:", date.today())

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))

try:
    print("Division:", divide(10, 2))
except ValueError as error:
    print("Error:", error)
