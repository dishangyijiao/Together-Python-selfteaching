import re
import operator
import collections
text='''
You jump, I jump!
My heart will go on.
To make each day count.
I'll never let go,I'll never let go,Jack.
Outwardly,I was everything a well-brought up girl should be.Inside,I was screaming.
Winning that ticket, it is the luckiest thing in my life, so I know you, know you really honored, very honored, you must help me, promise me to live, promise me you will not give up ... no matter what happens, Whatever the environment, Rose, promise me, do not forget……'''

text_words = re.sub(r'\W', " ", text)
words = text_words.split()
words_count = { word: words.count(word) for word in words }
sorted_words = sorted(words_count.items(), key=lambda kv: kv[1], reverse=True)
print(sorted_words)
