import random
import statistics

# 평균
a = [random.randint(0, 100) for i in range(10)]
print(a)
mean_of_a = statistics.mean(a)
print(mean_of_a)

# 중앙값
b = [random.randint(0, 100) for i in range(11)]  # 홀수개
c = [random.randint(0, 100) for i in range(10)]  # 짝수개
# 중앙값은 정렬을 전재로한다.
b = sorted(b)
c = sorted(c)
# 중앙값 추출
print(statistics.median(b))  # 홀수개일 경우 값이 정확히 맞아떨어지기 때문에 정수형태로 나온다.
print(statistics.median(c))  # 반면 짝수개일경우 n/2번째 값과 (n/2)+1번째 값의 평균이기 때문에 소수형태로 나온다.
