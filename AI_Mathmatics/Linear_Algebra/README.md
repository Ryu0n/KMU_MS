# 선형시스템 이론 및 실습
## 선형시스템 소개
우리가 초중등과정에서 배운 다항함수나 (미지수를 소거하는)연립방정식같은 개념들은 결국 선형시스템 안에 속한다. 
단지 미지수의 개수가 적을 뿐이다. 우리의 궁극적인 목적은 미지수의 갯수가 많을 경우 선형시스템을
사용하여 해를 구하는 것이다. 이러한 방법은 **가우스 소거법**을 통해 아무리 미지수가 많아도 시스템적으로 해결할 수 있는 
로직이 있다.  

선형대수의 목적은 어떤 연립일차방정식, 즉 **선형시스템을 정형적인 방법으로 표현하고 해결하는 방법**을 배우는 것이다.  


## 선형시스템의 구성요소
다음과 같은 **선형시스템**(linear system)이 있다고 가정해보자.  
```
3x + y + z = 4
x - 2y - z = 1
x + y + z = 2
```
이때 각각의 방정식들을 **선형방정식**(linear equation)이라고 한다. 즉, 선형시스템은 여러개의 선형방정식들로 구성된 것이다.  

그리고 우리가 이 선형시스템에서 알아내기 위한 미지수 x, y, z가 있다. 이 미지수들은 **unknown 혹은 variable** 이라고 한다.  

3개의 linear equation 과 3개의 unknown 으로 구성된 것을 3 x 3 linear system 이라고 표현한다.  

```
ex)
1 x 2 linear system)
3x + y + z = 4
x - 2y - z = 1

1 x 2 linear system)
2x + y = 3

3 x 2 linear system)
3x + y = 2
x - 2y = 3
2x - 4y = 6

non linear equation)
sin(x) + y = 2

non linear equation)
3x + y^3 = 2

non linear equation)
xy + z = 3
위의 방정식의 xy항(쌍곡선)은 실제로 미지수로 따지면 2승에 해당하기 때문에 비선형방정식이다.
```
## 선형시스템의 표현 (연립일차방정식의 대수적 표현)
대수적인 표현은 **Ax = b** 형태로 표현하는 것을 의미한다.  
```
3x + y = 2
x - 2y = 3
2x - 4y = 6
```
다음과 같은 3 x 2 linear system 이 있다고 가정해보자. 대수적 표현을 하기 위해서는 우선
1. linear system 의 unknown 들을 모아 **column vector(x)** 로 표현한다. **미지수벡터**라고도 한다.
2. 각 linear equation 의 coefficients(계수)들을 모아 **row vector(A)** 로 표현한다. **계수행렬**이라고도 한다.
3. constant(상수)들을 모아 **b** 로 표현한다. **상수벡터**라고도 한다.  

```
linear system의 대수적 표현)

|3  1|  |x|   |2|
|1 -1|      = |3|
|2 -4|  |y|   |6|

  A      x  =  b
```

## 선형시스템의 해 구하기
선형시스템을 대수적으로 표현할 경우 Ax = b 형태로 표현할 수 있다. 이 경우 각 요소는 수가 아닌 
행렬의 형태를 지니고 있다. 우리가 알고자 하는 것은 미지수 형태인 x 벡터이다. 고로, 양변에 계수행렬의 역행렬인
A^-1을 곱하면 된다.  
```
Ax = b
A^-1 * A * x = A^-1 * b
x = A^-1 * b
(*는 행렬곱을 의미한다.)
```

# 선형시스템의 해 구하기 (가우스 소거법 - Gauss Elimination)
## 선형시스템의 해
선형시스템의 해의 경우는 크게 3가지로 분류된다.  
1. 해가 하나일 경우 (unique solution)  
   eg) 3x = 6
2. 해가 존재하지 않는 경우 (no solution)  
   eg) 0x = 6
3. 해가 여러개인 경 (infinitely many solutions)  
   eg) 0x = 0
   
2번과 3번같이 a가 0일 경우 **특이**(**singular**)하다고 표현한다. a에 대한 역수가 존재하지 않기 때문이다.  

해가 존재하는 경우는 linear system 이  **consistent** 하다 표현하고, 존재하지 않으면 **inconsistent** 하다고 표현한다.

행렬도 위와 마찬가지이다.  
```
해가 하나인 경우(consistant)

|1  3| |x1|   |2|
|    | |  | = | |
|-2 1| |x2|   |3|

해가 없는 경우(inconsistant) & 역행렬이 존재하지 않음(singular)

|1 3| |x1|   |2|
|   | |  | = | |
|2 6| |x2|   |5|

해가 여러개인 경우(consistant) & 역행렬이 존재하지 않음(singular)

|1 3| |x1|   |2|
|   | |  | = | |
|2 6| |x2|   |4|
```

## 가우스 소거법 (Gauss Elimination)
가우스 소거법은 m x n linear system 의 해를 구하는 대표적인 방법이다. 가우스 소거법은 다음 두 단계로 진행된다.
1. 전방소거법 (Forward elimination) : 주어진 선형시스템을 아래로 갈수록 더 단순한 형태의 선형방정식을 가지도록 변형한다.  

우리가 선형시스템에서 해를 바로 구하지 못하는 이유는 계수행렬의 수가 너무 많기 때문이다. 그래서 그 수를 Forward 방향으로 줄이는 것이 목표이다.
Forward 방향은 기본적으로 **계수행렬의 위에서 아래방향, 왼쪽에서 오른쪽 방향**으로 정의한다.
그럼 다음과 같은 형태의 linear system 을 볼 수 있을 것이다.  
```
|?1 ?2 ?3| |x1|   |?a|
|0  ?4 ?5| |x2| = |?b|
|0   0 ?6| |x3|   |?c|
```
전방소거법을 마친 상태에서 가장 아래의 선형방정식을 확인해보면 ?6 * x3 = ?c 형태의 아주 간단한 방정식이 되어있을 것이다.


2. 후방대입법 (Back-substitution) : 아래서부터 위로 미지수를 실제 값으로 대체한다.
```
|?1 ?2 ?3| |x1|   |?a|
|0  ?4 ?5| |x2| = |?b|
|0   0 ?6| |x3|   |?c|
```
(?1 ~ ?6, ?a ~ ?c 는 전부 상수라 가정)  
다음과 같은 linear system 이 있을 때 최하단의 linear equation 을 통해 x3를 구하는 것은 아주 쉬운 일이다.
그 위의 linear equation 에 x3를 대입하면 x2 또한 쉽게 구할 수 있다. 마찬가지로 최상단의
linear equation 에 앞서 구한 x2와 x3를 대입하면 x1도 쉽게 구할 수 있다.

### 기본행연산 (ERO - Elementary Row Operations)
전방소거법은 **기본행연산**을 기반으로 하고 있다.  

<img width="512" alt="image" src="https://user-images.githubusercontent.com/32003817/110230040-37317a00-7f51-11eb-9093-d55302039a53.png">  

1. Interchange (교환)
2. Scaling (스케일링)
3. Replacement (치환)

### 전방소거법 예시

```
|1 2  1| |x1|   | 1| -> r1
|1 2  3| |x2| = | 3| -> r2
|2 3 -1| |x3|   |-3| -> r3
```
다음과 같은 linear system이 있다고 가정할 때, 전방소거법을 먼저 진행해보자.
우선 우리는 **주대각이 1이고, 그 아래의 수는 0**으로 바꾸어 역삼각형 형태의 행렬을 만드는 것이 목적이다.
2번 행(r2)에서 1번 행(r1)을 빼면 다음과 같은 형태로 변할 것이다.

```
<< R12(-1) :  r2 = r2 - r1 >>

|1 2  1| |x1|   | 1|
|0 0  2| |x2| = | 2|
|2 3 -1| |x3|   |-3|
```
이로써 주대각선의 첫 번째 요소에 해당하는 (1, 1)요소의 값을 1로, 그 밑의 (1, 2)요소의 값을 0으로 바꾸었다.
(1, 3)요소의 값을 0으로 바꿀 차례이다.
r3에서 r1에 2를 곱하여 빼면 (1, 3)요소가 0으로 소거될 것이다.

```
<< R13(-2) : r3 = r3 - 2*r1 >>

|1  2  1| |x1|   | 1|
|0  0  2| |x2| = | 2|
|0 -1 -3| |x3|   |-5|
```
그러나 지금 주대각선의 두 번째 요소인 (1, 2)요소가 0이므로 값을 존재하게 하기 위해 r2와 r3의 자리를 바꾼다.

```
<< R23 : r2 <-> r3 >>

|1  2  1| |x1|   | 1|
|0 -1 -3| |x2| = |-5|
|0  0  2| |x3|   | 2|
```
주대각선의 두 번째 요소(1, 2)를 1로 맞추기 위해 r2에 -1을 곱한다.

```
<< R2(-1) : r2 = r2 * (-1) >>

|1  2  1| |x1|   |1|
|0  1  3| |x2| = |5|
|0  0  2| |x3|   |2|
```
주대각선의 세 번째 요소(1, 3)를 1로 맞추기 위해 r3에 (1/2)를 곱한다.

```
<< R3(1/2) : r3 = r3 * (1/2) >>

|1  2  1| |x1|   |1|
|0  1  3| |x2| = |5|
|0  0  1| |x3|   |1|
```
계수행렬(row vector)이 상삼각형태(upper triangular form)로 변형된 모습다. 

### 후방대입법 예시
```
|1  2  1| |x1|   |1|
|0  1  3| |x2| = |5|
|0  0  1| |x3|   |1|
```
전방소거법을 통해 다음과 같은 형태의 계수행렬(row vector)을 만들었다. 이제 unknown에 실제 상수를 대입하는 과정이다.
r3를 보면 x3 = 1인 것을 바로 알 수 있기 때문에 미지수벡터(column vector)의 x3에 대입한다.  

```
|1  2  1| |x1|   |1|
|0  1  3| |x2| = |5|
|0  0  1| | 1|   |1|
```
r2 = x2 + 3 = 5 이므로 x2는 2임을 바로 알 수 있다.  

```
|1  2  1| |x1|   |1|
|0  1  3| | 2| = |5|
|0  0  1| | 1|   |1|
```
r3 = x1 + 4 + 1 = 1 이므로 x1은 -4임을 바로 알 수 있다.

```
|1  2  1| |-4|   |1|
|0  1  3| | 2| = |5|
|0  0  1| | 1|   |1|
```
최종적으로 column vector를 구한 상태이다.  

### 전방소거법의 가치
1. 주어진 linear system 을 가장 풀기 쉬운 형태로 변형해준다.
2. 주어진 linear system 의 rank 를 알려준다.
3. linear system 에 해가 있는지 (consistent) 없는지 (inconsistent) 알려준다.

#### Rank
전방소거법(forward elimination)을 마친 row vector 가 0으로 이루어진 row를 제외한 row의 갯수이다.
이것이 필요한 이유는?  

예를 들어보자.
```
rank = 2)

| 1 3| |x1|   |2|  forward elimination  | 1 3| |x1|   |2|
|    | |  | = | |  -------------------> |    | |  | = | |
|-2 1| |x2|   |3|                       | 0 1| |x2|   |1|
```

```
rank = 1)

|1 3| |x1|   |2|  forward elimination  | 1 3| |x1|   |2|
|   | |  | = | |  -------------------> |    | |  | = | |
|2 6| |x2|   |4|                       | 0 0| |x2|   |0|
```
두 linear system 모두 2개의 linear equation 과 2개의 unknown 이 존재하기 때문에
2 by 2 linear system 이다. 하지만 두 번째 linear system 을 forward elimination 한
결과 첫 번째 linear equation 을 두 배하면 두 번째 linear equation 이 나오므로 **실질적으로 
하나의 linear equation 이 존재**하는 것이나 다름없다. 이 경우 rank 가 1이라고 정의한 것이다.

#### Notice Consistent / Inconsistent
```
Consistent)

|1 3| |x1|   |2|  forward elimination  | 1 3| |x1|   |2|
|   | |  | = | |  -------------------> |    | |  | = | |
|2 6| |x2|   |4|                       | 0 0| |x2|   |0|
```
forward elimination 을 마친 마치막 linear equation 을 보면
0x1 + 0x2 = 0 인 것을 알 수 있다. 이는 어떠한 x1, x2를 대입하여도
만족하다는 의미이기 때문에 해가 무수히 많을 뿐 존재한다는 것을 알 수 있다.

```
Inconsistent)

|1 3| |x1|   |2|  forward elimination  | 1 3| |x1|   |2|
|   | |  | = | |  -------------------> |    | |  | = | |
|2 6| |x2|   |5|                       | 0 0| |x2|   |1|
```
반면 forward elimination 을 마친 마치막 linear equation 을 보면
0x1 + 0x2 = 1 다. 이는 어떠한 x1, x2를 대입하여도
만족할 수 없는 의미이기 때문에 해가 존재하지 않는다는 것을 알 수 있다.  

# LU 분해 (LU Decomposition)
## LU 분해의 정의
LU 분해는 **Gauss Elimination 을 행렬이라는 자료구조로 표현한 것**을 의미한다.
숫자는 인수분해가 가능하다. 행렬도 숫자와 마찬가지로 분해가 가능하다. 행렬을 분해하는 방법에는 대표적으로 세 가지가 있다.
* LU Decomposition
* QR Decomposition
* SVD (Singular Value Decomposition) : 특이값 분해  

QR Decomposition과 SVD는 직교분할과 관련이 있다.  

LU 분해는 인수분해를 하듯 **Lower triangular matrix**와 **Upper triangular matrix**의 곱으로 분해하는 것이다.  
```
|* * *| LU Decomposition  |* 0 0| |* * *|
|* * *| ----------------> |* * 0| |0 * *|
|* * *|                   |* * *| |0 0 *|
                             L       U
```
이 과정은 실제로 Gauss Elimination의 Forward Elimination과 밀접한 관련이 있다. 
Upper triangular matrix는 **Forward Elimination의 결과물**에 해당하고, 
Lower triangular matrix는 **Forward Elimination을 수행하는 과정**을 행렬로써 표현한 것이다.  

## LU 분해의 장점
**Ax = b** 형태의 linear system이 있다고 가정해보자. 우리의 궁극적인 목표는 *x를 구하는 것*이다.  

A row vector를 LU Decomposition이 가능하다고 가정하면,
**LUx = b** 과 같은 형태로 표현할 수 있다. 결합법칙을 적용하여 **L(Ux) = b**로 표현할 수 있다. Ux를 하나의 벡터 y로 가정하면
**Ly = b**로 정의할 수 있다.  

```
(b는 상수로 이루어진 벡터)

Ax = b
|* * *| |x1|   |b1|
|* * *| |x2| = |b2|
|* * *| |x3|   |b3|

LUx = b
|* * *| LU Decomposition  |* 0 0| |* * *|
|* * *| ----------------> |* * 0| |0 * *|
|* * *|                   |* * *| |0 0 *|
                             L       U

단, Ux = y
|* * *| |x1|   |y1|
|0 * *| |x2| = |y2|
|0 0 *| |x3|   |y3|
              
L(Ux) = b  -> Ly = b
|* 0 0| |y1|   |b1|
|* * 0| |y2| = |b2|
|* * *| |y3|   |b3|
```
위 행렬을 보면 알 수 있듯이 Ly = b 형태를 이용하면, **전방대치법(Forward-substitution)을 통해 y 벡터**를 구할 수 있다.
그리고, **y 벡터를 Ux = y에 실제값으로써 대입하면 x 벡터**도 쉽게 구할 수 있다.  

## LU 분해의 의미
* L : A row vector를 전방소거하는데 쓰인 **replacement와 scaling에 대한 EROs**를 기록한 행렬
* U : A row vector를 전방소거 한 후 남은 **upper triangular matrix**
* P(Permutation) : A row vector를 전방소거하는데 쓰인 **interchange에 대한 EROs**를 기록한 행렬 (Optional)

## LU 분해의 활용
* 수치적 안정성 : 선형시스템 Ax = b의 해를 A^-1을 통해 직접 구하는 것 보다 PLU분해를 사용하는 것이 수치적으로 안정적이다.
* b가 자주 업데이트되는 경우 : 선형시스템 Ax = b에서 A는 고정되어 있고 b가 업데이트되는 경우가 자주 있다.
이런 경우 행렬 A를 PLU로 미리 분해해놓으면 b가 업데이트될때마다 실시간으로 해 x를 구할 수 있다.  
  (y 구할때 forward-substitution, x 구할때 back-substitution) 
