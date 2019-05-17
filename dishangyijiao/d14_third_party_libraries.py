# 引用jieba第三方库 https://github.com/fxsjy/jieba/
import jieba
import json
import collections
import re

# 读取文件
with open('/Users/zh/Together-Python-selfteaching/dishangyijiao/tang300.json', 'r') as myfile:
  data = myfile.read()

# 解析文件
obj = json.loads(data)

# 转换为string
fullStr = '_'.join([str(elem) for elem in obj ])

# 找出所有中文 list
text_cn_list = re.findall(r'[\u4e00-\u9fa5]+', fullStr)

# 转换为string
text_cn_string =''.join(text_cn_list)

# 使用jieba的精确模式，找出对应中文分词
seg_list = jieba.cut(text_cn_string, cut_all=False)

# 转换为string
text_cn = " ".join(seg_list)

# 转换为list
words_cn = text_cn.split()

# 仅统计长度大于2的词
words_cn_length_greater_than_two = [i for i in words_cn if len(i) > 2]

# 统计词频，并输出前20的结果
cnt = collections.Counter()
for word in words_cn_length_greater_than_two:
  cnt[word] += 1
print(cnt.most_common(20))
