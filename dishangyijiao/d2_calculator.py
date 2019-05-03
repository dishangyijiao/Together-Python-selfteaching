# 使用Python编写一个支持加减乘除的计算器,支持输入参数,输出结果

def add(x, y):
  return x + y

def substract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

print("""\
Select operation.
  1.Add
  2.Substract
  3.Multiply
  4.Divide
""")

choice = input("Enter choice(1/2/3/4)")

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

if choice == "1":
  print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == "2":
  print(num_1, "-", num_2, "=", substract(num_1, num_2))
elif choice == "3":
  print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == "4":
  print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
  print("Invalida input")
