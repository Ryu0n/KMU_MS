# 컴퓨팅
## 컴퓨팅 서비스 개요
![img.png](img.png)  
AWS는 이 모듈에서 다루는 많은 컴퓨팅 서비스를 제공한다.  
* Amazon Elastic Compute Cloud (EC2)  
크기 조정이 가능한 가상 머신을 제공한다.  
  
* Amazon EC2 Auto Scaling  
EC2 인스턴스를 자동으로 시작하거나 종료하는 조건을 정의할 수 있도록 하여 애플리케이션 가용성을 지원한다.

* Amazon Elastic Container Registry (ECR)  
Docker 이미지를 저장하고 검색하는 데 사용된다.  
  
* Amazon Elastic Container Service (ECS)  
Docker를 지원하는 컨테이너 오케스트레이션 서비스이다.  
  
* VMware Cloud on AWS  
맞춤형 하드웨어 없이 하이브리드 클라우드를 프로비저닝할 수 있다.  
  
* AWS Elastic Beanstalk  
감편하게 웹 애플리케이션을 실행하고 관리할 수 있는 서비스
  
* AWS Lambda  
서버리스 컴퓨팅 솔루션으로 사용한 컴퓨팅 시간에 대해서만 비용을 지불한다.
  
* Amazon Elastic Kubernetes Service (EKS)  
AWS 에서 관리형 Kubernetes를 실행할 수 있다.
  
* Amazon Lightsail  
애플리케이션 또는 웹 사이트를 구축할 수 있는 간편한 서비스를 제공한다.

* AWS Batch  
규모에 관계없이 배치 작업을 실행할 수 있는 도구를 제공
  
* AWS Fargate  
서버 또는 클러스터를 관리해야 하는 부담이 적은 컨테이너를 실행하는 서비스를 제공  
  
* AWS Outpost  
온프레미스 데이터 센터에서 엄선된 AWS 서비스를 실행할 수 있도록 지원
  
* AWS Serverless Application  
Repository를 사용하면 서버리스 애플리케이션을 검색, 배포 및 게시할 수 있다.  
  
## 컴퓨팅 서비스 분류
![img_1.png](img_1.png)  
컴퓨팅 서비스는 크게 가상 머신을 제공하는 컴퓨팅 서비스인 **서비스형 인프라**, **서버리스 컴퓨팅**, **컨테이너 기반 컴퓨팅**, 웹 애플리케이션을 위한 **서비스형 플랫폼**으로 정의되는 4가지 범주중 하나에 포함된다.
* 서비스형 인프라  
e.g) Amazon EC2  
  이 범주의 서비스는 유연성을 제공하며 서버 관리 작업의 많은 부분을 사용자가 맡아야 한다.
  운영체제는 물론 실행하는 서버의 크기 및 리소스 기능도 사용자가 선택한다.  
  
  
* 서버리스 컴퓨팅  
e.g) AWS Lambda (관리가 전혀 필요하지 않은 컴퓨팅 플랫폼)  
  AWS Lambda를 사용하면 서버를 프로비저닝하거나 관리하지 않고도 코드를 실행할 수 있다.
  사용한 컴퓨팅 시간ㅇ네 대한 요금만 지불한다. 서버리스 컴퓨팅의 인기가 높아지는 이유는 **클라우드 네이티브 아키텍처를 지원하기** 때문이다.
  클라우드 네이티브 아키텍처에서는 동일한 워크로드의 실행을 보장하기 위해 서비스를 상시 실행하는 것보다 저렴한 비용으로 대규모 확장 및 축소를 수행할 수 있다.  
  
* 컨테이너 기반 컴퓨팅  
e.g) Amazon Elastic Container Service, Amazon Elastic Kubernetes Service, AWS Fargate, Amazon Elastic Container Registry  
  컨테이너는 프로비저닝 프로세스에서 **운영 체제를 추상화**하기 때문에 가상머신보다 더 빠르게 프로비저닝된다.  
  
* 서비스형 플랫폼  
e.g) AWS Elastic Beanstalk (웹 애플리케이션을 위한)  
  AWS Elastic Beanstalk는 필요한 모든 애플리케이션 서비스를 제공하므로 배포가 가속화된다. 
  OS, 애플리케이션 서버 및 기타 인프라 구성 요소를 AWS가 관리하므로 사용자는 애플리케이션 코드 개발에 집중할 수 있다.  
  
## 최적의 컴퓨팅 서비스 선택
![img_2.png](img_2.png)  
단일 컴퓨팅 솔루션으로 시작한 다음 애플리케이션 설계의 사용량 패턴 또는 변경에 따라 설계를 완전히 변경할 수도 있다.


## Amazon EC2
## Amazon EC2 비용 최적화
## 컨테이너 서비스
## AWS Lambda
## AWS Elastic Beanstalk