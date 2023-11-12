import random
import itertools



a = ['김 승 현', '김 진 호', '강 춘 자', '이 예 준', '김 현 주']
b = ['청 소', '빨 래', '설 거 지']

random.shuffle(a)
result = itertools.zip_longest(a, b, fillvalue='휴식')
for r in result:
    print(r)
