while True:
  q1=input('请问甲，你认罪吗？请回答：认罪或者沉默  ')
  q2=input('请问乙，你认罪吗？请回答：认罪或者沉默  ')
  if q1 =='认罪' and q2 =='认罪':
    print ('两人都得判10年，唉，好好准备后事吧！')
  elif q1=='认罪' and q2=='沉默':
    print ('甲判1年，乙判20年')
  elif q1=='沉默' and q2=='认罪':
    print('甲判20年，乙判1年')
  else:
    print ('你们两人都判3年，皆大欢喜！')
    break

