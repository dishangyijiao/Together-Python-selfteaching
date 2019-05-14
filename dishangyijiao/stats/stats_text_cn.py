def stats_text_cn(text_cn):
  if isinstance(text_cn, str):
    # 统计每个汉字的出现次数
    words_cn_count = { word: text_cn.count(word) for word in text_cn }
    # 按照汉字的出现次数倒序排序
    sorted_words_cn = sorted(words_cn_count.items(), key=lambda kv: kv[1], reverse=True)
    # 将倒序的结果输出
    print(sorted_words_cn)
  raise ValueError('text is not a string')