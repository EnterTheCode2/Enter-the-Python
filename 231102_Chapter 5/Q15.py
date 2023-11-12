
import itertools

cleaning = ['구광모', '구본준', '권영수', '신학철']
result = itertools.combinations(cleaning, 2)

print(list(result))
