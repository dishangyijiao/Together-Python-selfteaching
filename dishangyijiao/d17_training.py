import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import requests
from pyquery import PyQuery
import jieba
import collections
import re
from wxpy import *

bot = Bot()
my_friends = bot.friends()
@bot.register(my_friends, SHARING)

def auto_reply(msg):
  msg.reply('收到消息')

  response = requests.get(msg.url)
  document = PyQuery(response.text)
  content = document('#js_content').text()
  document_list = re.findall(r'[\u4e00-\u9fa5]+', content)
  document_string = "".join(document_list)
  content_list = jieba.cut(document_string, cut_all=False)
  document_cn = " ".join(content_list)
  words_cn = document_cn.split()

  cnt = collections.Counter()
  for word in words_cn:
    cnt[word] += 1
  result = cnt.most_common(10)
  objects = []
  performance = []
  for word in result:
    objects.append(word[0])
    performance.append(word[1])

  # 生成图片
  y_pos = np.arange(len(objects))
  plt.bar(y_pos, performance, align='center', alpha=0.5)
  plt.xticks(y_pos, objects)
  plt.ylabel('times')
  plt.title('words appear')

  # 保存为png格式,并对图片进行处理
  plt.savefig('foo.png', bbox_inches='tight')

  msg.reply_image('foo.png')
embed()
