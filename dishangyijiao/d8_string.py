import re
text = '''
You jump, I jump.
My heart will go on.
To make each day count.
I'll never let go,I'll never let go,Jack.
Outwardly,I was everything a well-brought up girl should be.Inside,I was screaming.
Winning that ticket, it is the luckiest thing in my life, so I know you, know you really honored, very honored, you must help me, promise me to live, promise me you will not give up ... no matter what happens, Whatever the environment, Rose, promise me, do not forget.'''

text_1 = text.lower().replace('jump', 'happy')
text_2 = re.sub(r'\b\S?no?\S\b', "", text)
text_3 = text_2.swapcase()
words = text_3.split()
words.sort()
for word in words:
  print(word)