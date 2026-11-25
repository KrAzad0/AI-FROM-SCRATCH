import math
text="2+2=4\n"*50
vocab=sorted(set(text)); n=len(vocab); ids={c:i for i,c in enumerate(vocab)}
w=[[0.0]*n for _ in vocab]
def softmax(x):
    z=[math.exp(t-max(x)) for t in x]; return [t/sum(z) for t in z]
for epoch in range(12):
    loss=0
    for a,b in zip(text,text[1:]):
        i,j=ids[a],ids[b]; p=softmax(w[i]); loss-=math.log(p[j])
        for k in range(n): w[i][k]-=0.05*(p[k]-(k==j))
    print(epoch,loss/(len(text)-1))
print(dict(zip(vocab,softmax(w[ids["="]]))))
