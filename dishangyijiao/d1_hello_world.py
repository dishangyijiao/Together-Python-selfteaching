
print("Python Hello World")

# Convert binary to decimal

binary_num = list(input("Input a binary number: "))
value = 0
for i in range(len(binary_num)):
  digit = binary_num.pop()
  if digit == "1":
    value = value + pow(2, i)
print("The decimal value of the number is", value)

# 110101 => 53