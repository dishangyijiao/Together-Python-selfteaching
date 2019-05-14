from stats.stats_text_cn import stats_text_cn

text = 2
try:
  stats_text_cn(text)
except ValueError as err:
  print(err.args)