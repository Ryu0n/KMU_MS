# AlexNet
AlexNet은 2012년에 개최된 **ILSVRC(ImageNet Large Scale Visual Recognition Challenge) 대회의 우승을 차지**한 컨볼루션 신경망(CNN) 구조이다. 
CNN의 부흥에 아주 큰 역할을 한 구조라고 말할 수 있다. AlexNet의 original 논문명은 "ImageNet Classification with Deep Convolutional Neural Networks"이다. 
이 논문의 첫번째 저자가 Alex Khrizevsky이기 때문에 그의 이름을 따서 AlexNet이라고 부른다. 

AlexNet의 기본구조의 특징은 **2개의 GPU로 병렬연산**을 수행하기 위해서 병렬적인 구조로 설계되었다는 점이 가장 큰 변화이다.  

## Overall structure
![img.png](img.png)  
위 그림은 AlexNet의 구조도이다. **5개의 컨볼루션 레이어와 3개의 full-connected 레이어**로 구성되어 있다. 
두번째, 네번째, 다섯번째 컨볼루션 레이어들은 전 단계의 같은 채널의 특성맵들과만 연결되어 있는 반면, 
**세번째 컨볼루션 레이어는 전 단계의 두 채널의 특성맵들과 모두 연결되어 있다.**  

local response normalization는 수렴 속도를 높이기 위해 시행된다.

## Calculate feature map size
![img_1.png](img_1.png)  
S : 보폭  
H : 이미지의 높이, P : Padding size, Fh = 필터의 높이  
W : 이미지의 너비, P : Padding size, Fw = 필터의 너비  
ex) ((55 + 2*1 - 5) / 2) + 1 = (52 / 2) + 1 = 26 + 1 = 27

## Activation function
AlexNet 이전에 사용되던 활성함수들은 하이퍼볼릭 탄젠트나 시그모이드와 같은 saturating nonlinearities가 사용되었는데
Rectified Linear Unit (ReLU)와 같은 non-saturating nonlinearity 활성함수를 사용하자 학습시간이 비약적으로 빨라졌다.

# VGGNet
VGGNet은 옥스포드 대학의 연구팀 VGG에 의해 개발된 모델로써, **2014년 이미지넷 이미지 인식 대회에서 준우승**을 한 모델이다. 
여기서 말하는 VGGNet은 16개 또는 19개의 레이어로 구성된 모델을 의미한다(VGG16, VGG19로 불림). 
AlexNet과 다른점이 있다면 **병렬적 구조로 이뤄지지 않았다.**  

## Depth
![img_2.png](img_2.png)  
위 그림을 보면 알다시피 VGG 네트워크를 기점으로 **레이어의 깊이가 깊어질수록 에러율이 낮게 보이는 것**을 확인할 수 있다. 
이전까지는 8개의 레이어로 구성이 되었지만 VGG 네트워크부터는 16 혹은 19개의 레이어로 구성이 되고, GoogleNet은 22개, RestNet은 152개의 레이어로 구성이 되었다.

## Number of weight
VGGNet의 구조를 깊이 들여다보기에 앞서 먼저 집고 넘어가야할 것이 있다. 
그것은 바로 3 x 3 필터로 두 차례 컨볼루션을 하는 것과 5 x 5 필터로 한 번 컨볼루션을 하는 것이 결과적으로 동일한 사이즈의 특성맵을 산출한다는 것이다(아래 그림 참고). 
3 x 3 필터로 세 차례 컨볼루션 하는 것은 7 x 7 필터로 한 번 컨볼루션 하는 것과 대응된다.

![img_3.png](img_3.png)  

그러면 3 x 3 필터로 세 차례 컨볼루션을 하는 것이 7 x 7 필터로 한 번 컨볼루션하는 것보다 나은 점은 무엇일까? 
일단 가중치 또는 파라미터의 갯수의 차이다. 3 x 3 필터가 3개면 총 27개의 가중치를 갖는다. 
반면 7 x 7 필터는 49개의 가중치를 갖는다. CNN에서 가중치는 모두 훈련이 필요한 것들이므로, 가중치가 적다는 것은 그만큼 훈련시켜야할 것의 갯수가 작아진다. 따라서 학습의 속도가 빨라진다. 
동시에 층의 갯수가 늘어나면서 특성에 비선형성을 더 증가시키기 때문에 특성이 점점 더 유용해진다.  

-> 가중치의 수는 필터의 원소 수를 의미한다. (필터는 가중치의 집합이기 때문). 고로 3 x 3 필터(가중치 9개)로 3번의 컨볼루션 연산을 수행하면 27개((9개 * 3 = 27)의 가중치가 나온다.
반면, 7 x 7 필터는 한번밖에 사용하지 않았음에도 불구하고 필터의 변의 길이 제곱이므로 가중치의 수가 기하급수적으로 많아진다. 

## Overall structure
![img_4.png](img_4.png)  


# GoogleNet

# RestNet