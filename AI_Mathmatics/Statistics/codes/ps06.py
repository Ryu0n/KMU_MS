import numpy as np

# sample mean
samples = [9, 4, 0, 8, 1]
print(np.mean(samples))

# sample mean, standard deviation
w = [10.7, 11.7, 9.8, 11.4, 10.8, 9.9, 10.1, 8.8, 12.2, 11.0, 11.3,
     11.1, 10.3, 10.0, 9.9, 11.1, 11.7, 11.5, 9.1, 10.3, 8.6, 12.1,
     10.0, 13.0, 9.2, 9.8, 9.3, 9.4, 9.6, 9.2]

xbar = np.mean(w)
sd = np.std(w, ddof=1)
print('평균 %.2f, 표준편차 %.2f' %(xbar, sd))

# 신뢰구간 추정
import math
import scipy.stats
alpha = 0.05
zalpha = scipy.stats.norm.ppf(1-alpha/2)
print('zalpha : ', zalpha)
print('min : ', xbar - zalpha*sd/math.sqrt(len(w)), 'max : ', xbar + zalpha*sd/math.sqrt(len(w)))

# 모비율 추정
x = 48
n = 150
phat = x / n
alpha = 0.05
zalpha = scipy.stats.norm.ppf(1-alpha/2)
sd = np.sqrt((phat * (1-phat))/n)
ci = [phat - zalpha*sd, phat + zalpha*sd]
print('phat %.3f, zalpha %.3f, sd %.3f' %(phat, zalpha, sd))
print(ci)
