import collections
text_en = '''
If we can only encounter each other rather than stay with each other then I wish we had never encountered
'''

def stats_text_en(text_en):
  if isinstance(text_cn, str):
    # 转换为数组字符串
    words_en = text_en.split()
    # # 统计每个单词的出现次数
    # words_en_count = { word: words_en.count(word) for word in words_en }
    # # 按照单词出现次数的倒序排序
    # sorted_words_en = sorted(words_en_count.items(), key=lambda kv: kv[1], reverse=True)
    # # 将倒序的结果输出
    # print(sorted_words_en)

    # 使用Python标准库中的Counter进行优化
    cnt = collections.Counter()
    for word in words_en:
      cnt[word] += 1
    print(cnt)
  raise ValueError('text is not a string')


text_cn = '''
边 实 践 边 学 习 边 总 结
'''
def stats_text_cn(text_cn):
  if isinstance(text_cn, str):
    # 字符串转换为数组字符串
    words_cn = text_cn.split()
    # # 统计每个汉字的出现次数
    # words_cn_count = { word: words_cn.count(word) for word in words_cn }
    # # 按照汉字的出现次数倒序排序
    # sorted_words_cn = sorted(words_cn_count.items(), key=lambda kv: kv[1], reverse=True)
    # # 将倒序的结果输出
    # print(sorted_words_cn)
    cnt = collections.Counter()
    for word in words_cn:
      cnt[word] += 1
      print(cnt)
  raise ValueError('text is not a string')