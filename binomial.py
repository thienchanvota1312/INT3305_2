import math

def giaiThua(x):
    i = 0
    result = 1
    for i in range(1, x+1):
        result = result*i;
    return result;

def prob(n, p, N):
    return (giaiThua(N))/((pow(p,n))*giaiThua(n)*giaiThua(N-n));

def infoMeasure(n, p, N):
    return -math.log(prob(n,p,N),2)

def sumProb(n, p, N):
    i = 0
    sum = 0
    for i in range(1, n+1):
        sum = sum + prob(i, p, N)
    return sum

def approxEntropy(n, p, N):
    i = 0;
    sum = 0
    averageInfor = 0
    for i in range(1, n+1):
        sum = sum + infoMeasure(i, p, N)
    averageInfor = sum/n;
    return averageInfor;
