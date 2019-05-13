def stats_text_en(text_en):
  # 统计每个单词的出现次数
  words_en_count = { word: text_en.count(word) for word in text_en }
  # 按照单词出现次数的倒序排序
  sorted_words_en = sorted(words_en_count.items(), key=lambda kv: kv[1], reverse=True)
  # 将倒序的结果输出
  print(sorted_words_en)