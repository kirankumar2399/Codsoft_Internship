
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice (1/2/3/4): "))


if choice == 1:
  result = add(num1, num2)
  print(num1, "+", num2, "=", result)
elif choice == 2:
  result = subtract(num1, num2)
  print(num1, "-", num2, "=", result)
elif choice == 3:
  result = multiply(num1, num2)
  print(num1, "*", num2, "=", result)
elif choice == 4:
  result = divide(num1, num2)
  print(num1, "/", num2, "=", result)
else:
  print("Invalid choice")
