# 通过Python的模块，引入已经写好的方法
from stats.stats_text_en import stats_text_en
from stats.stats_text_cn import stats_text_cn
# Python的调试工具
import pdb
# 在断点位置写入下面的命令
# pdb.set_trace()
# 引入Python的regular expression
import re

text='''
The way I see it, it’s hard to find a place in the world that requires the ability to learn more than trading markets. The success of almost any trade can be finally traced back to the ability to learn. Almost all badass traders are great learners and researchers.
People often use long-term and short-term to distinguish between “speculation” and “investment”, but this is very superficial. Speculation can also be long-term, just like investment can also be short-term. People see speculation as having a negative connotation, while investment as having a positive one, but this is also a common mistake and a superficial point of view. Which would you say would be better, a “failed investment” or a “successful speculation”? So, I won’t use concepts that are defined by “long-term” or “short-term”, whether for “speculation” or “investment”.
I personally distinguish between speculation and investment in this way:
Speculators refuse to learn, and investors are good at learning.
Before trading, research diligently and study deeply. After trading, whether you won or lost, you must review and summarize, correcting your ideas and thinking in order to improve your next decision. People who do this are investors in my eyes, even if they “enter and exit quickly”.
What about “leeks”? The don’t study, they don’t research, they only see what is under their nose, they blame everything but themselves… Whether or not people like this have money, whether or not they have a high IQ, they are all “failed speculators” in my eyes, and they are true dumbasses!
“在我看来，这世界上很难有哪一个地方比交易市场更需要学习能力了。几乎一切交易的成功，最终都可以溯源到学习能力上来。几乎所有的牛×交易者，都是学习和研究的高手。
人们常常用短期和长期来区分“投机”和“投资”，这是很肤浅的。投机也可以很长期，正如投资也可以很短期一样。人们对投机抱有贬义，对投资抱有褒义，也是普遍错误而又肤浅的想法。你说“失败的投资”和“成功的投机”，哪一个更好呢？所以，使用“长期”或者“短期”来定义的概念，无论是“投机”还是“投资”，都不是我会使用的。
我个人是这样区分投机者和投资者的：”
“投机者拒绝学习，投资者善于学习。
交易之前，认真研究，深入学习；交易过后，无论输赢，都要总结归纳，修正自己的观念和思考，以便完善下一次的决策——这么做的人，在我眼里都是投资者，哪怕他们是“快进快出”。
“韭菜”是什么样的呢？他们不学习，他们不研究，他们鼠目寸光，他们怨天尤人……这样的人，在我眼里无论有钱与否，无论智商高低，都是“失败的投机者”，是千真万确的傻×。”
'''
# 在text中匹配出所有英文单词
text_en = re.findall(r'[a-zA-Z0-9]+', text)
# 调用stats_text_en中的方法，输出结果
stats_text_en(text_en)
# pdb.set_trace() 调试用

# 在text中匹配出所有中文
text_cn = re.findall(r'[\u4e00-\u9fa5]+', text)
# 调用stats_text_cn中的方法，输出结果
stats_text_cn(text_cn)