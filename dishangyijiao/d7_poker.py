# 打印1副扑克牌（4种花色，2——10——JQKA）

poker_color = ["❤", "♦", "♣", "♠"]

poker_count = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

for x in poker_color:
  poker = [x + c for c in poker_count]
  print (poker)
