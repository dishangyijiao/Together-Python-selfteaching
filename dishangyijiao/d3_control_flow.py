# 1. 使用for循环打印九九乘法表

for row in range(1, 10):
  for col in range(1, row+1):
    print("{} * {} = {}\t". format(col, row, row * col), end = "")
  print()

# 2. 使用while循环打印九九乘法表，并把偶数行去掉

row = 1
while row <= 9:
  col = 1
  while col <= row:
    if row % 2 != 0:
      print("{} * {} = {}\t". format(col, row, row * col), end = "")
    col += 1
  print("")
  row += 1