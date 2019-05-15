import json
import pdb
import collecitons
# 读取文件
with open('/Users/zh/Together-Python-selfteaching/dishangyijiao/tang300.json', 'r') as myfile:
  data = myfile.read()
# pdb.set_trace()
# 解析文件
obj = json.loads(data)

# TODO 明天再处理中文词频输出
    cnt = collections.Counter()
    for word in words_cn:
        cnt[word] += 1
        print(cnt.most_common(count))


