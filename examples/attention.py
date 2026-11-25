import math
x=[[1.,0.],[0.,1.],[1.,1.]]
for i,q in enumerate(x):
    scores=[sum(a*b for a,b in zip(q,k))/math.sqrt(2) for k in x[:i+1]]
    e=[math.exp(s-max(scores)) for s in scores]; p=[v/sum(e) for v in e]
    out=[sum(a*v[j] for a,v in zip(p,x)) for j in range(2)]
    assert abs(sum(p)-1)<1e-10
    print(i,p,out)
