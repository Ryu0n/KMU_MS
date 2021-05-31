import numpy as np
import scipy.stats

w = [10.7, 11.7, 9.8, 11.4, 10.8, 9.9, 10.1, 8.8, 12.2, 11.0, 11.3,
     11.1, 10.3, 10.0, 9.9, 11.1, 11.7, 11.5, 9.1, 10.3, 8.6, 12.1,
     10.0, 13.0, 9.2, 9.8, 9.3, 9.4, 9.6, 9.2]

# 모평균 검정
# 가설에 의한 모평균
mu = 10.5
# 표본평균
xbar = np.mean(w)
# 표본표준편차
sd = np.std(w, ddof=1)
z = (xbar-mu)/(sd/np.sqrt(len(w)))
print('검정통계량 : ', z)

# 유의수준
alpha = 0.05
# 임계값
cri = scipy.stats.norm.ppf(1-alpha/2)
print('임계값 : ', cri)
