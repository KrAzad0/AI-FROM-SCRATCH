from itertools import product
for a,b,c in product(range(2),repeat=3):
    s=a^b^c
    carry=(a&b)|(c&(a^b))
    assert s+2*carry==a+b+c
    print(a,b,c,"->",carry,s)
