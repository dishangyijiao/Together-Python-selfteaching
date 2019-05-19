# 导入wxpy模块
from wxpy import *
import re
import requests
from pyquery import PyQuery
import jieba
import collections
# 初始化机器人，扫码登录
bot = Bot()

# 找到所有好友
my_friends = bot.friends()

# 监听好友消息
@bot.register(my_friends, SHARING)

# 回复消息
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
  msg.reply("{}". format(cnt.most_common(100)))
embed()
