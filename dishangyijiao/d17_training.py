import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# d15的结果
# words_ten = [('的', 1310), ('是', 473), ('一个', 407), ('我们', 307), ('我', 273), ('你', 218), ('了', 217), ('在', 211), ('有', 157), ('微信', 139)]
objects = ('的', '是', '一个', '我们', '我', '你', '了', '在', '有', '微信')
y_pos = np.arange(len(objects))
performance = [1310, 473, 407, 307, 273, 218, 217, 211, 157, 139]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('times')
plt.title('words appear')

plt.show()