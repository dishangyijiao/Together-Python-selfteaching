# 引用yagmail邮箱库
import yagmail
# 引用requests网络请求库
import requests
# 引用pyquery xml文档解析库
from pyquery import PyQuery
# 引用jieba中文词频分析库
import jieba
# 引用Python容器数据类型
import collections
# 引用Python正则
import re
# 引用调试
import pdb
# 输入密码
import getpass
# 张小龙 2019年微信公开课演讲
allen_zhang_url = "https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA"

# 通过requests进行get请求
response = requests.get(allen_zhang_url)

# 提取公众号伪代码
document = PyQuery(response.text)
content = document('#js_content').text()

# 找出所有中文
document_list = re.findall(r'[\u4e00-\u9fa5]+', content)

# 转换为string
document_string = "".join(document_list)

# 使用jieba的精确模式，找出对应中文分词
content_list = jieba.cut(document_string, cut_all=False)

# 将词频分析装换为string
document_cn = " ".join(content_list)

# 转换为list
words_cn = document_cn.split()

# 统计词频，输出前100个结果
cnt = collections.Counter()
for word in words_cn:
  cnt[word] += 1

# 输出结果转换为string
contents = "{}". format(cnt.most_common(100))
# 输入发件人和收件人信息
sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码(或授权码):')
recipients = input('输入收件人邮箱:')
yag = yagmail.SMTP(sender, password)
yag.send(to = recipients, subject = 'd15 词频统计', contents = contents)