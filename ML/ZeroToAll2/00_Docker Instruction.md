# Docker Instruction

이 글은 모두의 딥러닝 시즌2 강의를 정리했음을 밝힙니다.

## 개요

단순하게는 다른 사람의 컴퓨터(환경설정)에서는 잘 돌아가는 코드가 내 컴퓨터에서 안돌아가는 상황을 피하기 위해서 사용한다. 

좀 더 세부적으로 말하자면 애플리케이션을 작동시키기 위해 필요한 라이브러리나 애플리케이션등을 하나로 모아, 마치 별도의 서버인 것처럼 사용할 수 있게 만들기 하기 위해 **도커**를 사용한다.

도커를 사용하게 되면 가상화 머신처럼 독립된 운영체제를 여러개 띄울 필요가 없다. 같은 운영체제 위에 도커를 띄우게 되면 어느 컴퓨터에서도 돌아가는 가상환경을 여러개 띄울 수 있다. 

[이미지출처](https://www.google.co.uk/url?sa=i&source=images&cd=&ved=2ahUKEwjX9rijob7mAhXHFIgKHXO8Dk0QjRx6BAgBEAQ&url=https%3A%2F%2Fsubicura.com%2F2017%2F01%2F19%2Fdocker-guide-for-beginners-1.html&psig=AOvVaw2HFuRqQg4g0yF_dyA0ODmx&ust=1576726276227080)

![vm-vs-docker](assets/vm-vs-docker.png) 

## Docker의 장점

가상 머신은 완벽한 운영체제를 생성할 수 있다는 장점은 있지만, 일반 호스트에 비해 성능 손실이 있으며, 수 기가바이트에 달하는 가상 머신이미지를 애플리케이션으로 배포하기 부담스럽다는 단점이 있다.

>하이퍼바이저에 의해 생성되고 관리되는 운영체제는 **게스트 운영체제(Guest OS)**라고 하며, 각 게스트 운영체제는 다른 게스트 운영체제와는 완전히 독립된 공간과 시스템 자원을 할당받아 사용하게 된다. 그러나 각종 시스템 자원을 가상화하고 독립된 공간을 생성하는 작업은 하이퍼바이저를 반드시 거치게 되기 때문에 일반 호스트에 비해 **성능의 손실이 발생**하게 된다. 게다가 가상 머신은 게스트 운영체제를 사용하기 위한 라이브러리, 커널 등을 전부 포함하기 때문에 가성 머신을 배포하기 위한 이미지로 만들었을 때 **이미지의 크기** 또한 커지게 된다.

이에 비해 도커 컨테이너는 프로세스 단위의 격리 환경을 만들기 때문에 성능 손실이 거의 없다. 컨테이너에 필요한 커널은 **호스트의 커널을 공유해 사용**하고, 컨테이너 안에는 애플리케이션을 구동하는데 필요한 라이브러리 및 실행 파일만 존재하기 때문에 컨테이너를 **이미지로 만들었을 때의 크기가 대폭 줄어들게** 된다.

따라서 컨테이너를 이미지로 만들어 배포하는 시간이 가상머신에 비해 빠르며, 가상화된 공간을 사용할 때의 성능 손실도 거의 없다는 장점이 있다.

## Download for Windows

도커는 원래 리눅스 서버를 생각하고 만든 것이기 때문에 별도의 가상머신이나 하이퍼바이저를 사용하기 때문에 리눅스 만큼의 성능이 나오지 않고 GPU를 사용할 수 없다.

### 설치방법

사용 운영체제가 Windows 10 Pro(64-bit) 환경이므로 [Docker for Windows](https://runnable.com/docker/install-docker-on-windows-10)를 설치한다.

사이트에 나와있는 방법대로 설치 후에 

- 제어판 => 프로그램 및 기능 => Windows 기능 켜기/끄기 => Hyper-v 체크

bash창이나 cmd창에서 `docker run hello-world` 명령어로 잘 설치되었는지 확인한다.

기본 사용방법은 [Docker User Guide](https://github.com/deeplearningzerotoall/PyTorch/blob/master/docker_user_guide.md)를 참고한다.

