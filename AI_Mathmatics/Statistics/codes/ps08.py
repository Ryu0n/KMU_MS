import numpy as np


def cross_entropy(P, Q):
    return sum([-P[i]* np.log2(Q[i]) for i in range(len(P))])


P = [1, 0]
Q = [0.8, 0.2]
print(cross_entropy(P, Q))

Q = [0.5, 0.5]
print(cross_entropy(P, Q))

Q = [0.2, 0.8]
print(cross_entropy(P, Q))
