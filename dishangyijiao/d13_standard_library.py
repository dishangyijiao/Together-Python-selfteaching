import json
import pdb
import collections
import re
# 读取文件
with open('/Users/zh/Together-Python-selfteaching/dishangyijiao/tang300.json', 'r') as myfile:
  data = myfile.read()
# pdb.set_trace()
# 解析文件
obj = json.loads(data)
# 转换为string
fullStr = '_'.join([str(elem) for elem in obj ])
# 找出所有中文
text_cn = re.findall(r'[\u4e00-\u9fa5]+', fullStr)
# 输出结果
cnt = collections.Counter()
for word in text_cn:
  cnt[word] += 1
print(cnt.most_common(100))


