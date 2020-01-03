# calculates mean
def meanof(x):
    return (sum(x) / len(x))

# calculates covariance
def cov(x,y):
    xbar = meanof(x)
    ybar = meanof(y)
    sol = []

    for i,j in zip(x,y):
        sol.append((i - xbar)*(j - ybar))

    return (sum(sol) / (len(x) - 1))

# calculates variance
def var(x):
    xbar = meanof(x)
    sol = []

    for i in x:
        sol.append(pow((i - xbar),2))
    
    return (sum(sol) / (len(x) - 1))