#Q12

#이해가 잘 안된다. 다시 공부 하기


import random
result = []
while len(result) < 6:
    lotto = random.randint(1,45)
    if lotto not in result:
        result.append(lotto)

print(result)
