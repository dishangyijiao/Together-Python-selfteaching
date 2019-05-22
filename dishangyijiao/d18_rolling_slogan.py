import time
adv=input("请输入一段广告语：")
while 1:
    direction = input("请输入滚动的方向（L/R)").upper()
    if direction in ['L','R']:
      break
    print("您输入的有误，请重新输入！")
    
while 1:
    integer = input("请输入滚动的速度（请输入一个整数）:")
    if integer.isnumeric():
      break
    print("您输入的有误，请重新输入！")
while 1:
    if direction == "R":
      adv = adv[-1] + adv[:-1]
    else:
      adv = adv[1:] + adv[0]
    print('\r'+adv,end='',flush=True)
    time.sleep(int(integer))