# Docker 명령어 정리

## 자주 쓰이는 기본 명령어

* `docker -v`: 도커 엔진 버전 확인
* `docker images`: 도커 엔진에 존재하는 이미지의 목록을 출력
* `docker start [container_name]`: 해당 컨테이너 이름을 가진 컨테이너 가동
* `docker stop [container_name]`: 컨테이너 정지
* `docker attach [container_name]`: 해당 컨테이너 이름을 가진 컨테이너 내부로 들어감
* `docker ps`: 정지되지 않은 컨테이너의 목록 확인
* `docker ps -a`: 정지된 컨테이너를 포함한 모든 컨테이너 목록 확인
* `docker rename [current_container_name] [new_container_name]`: 컨테이너의 이름을 변경
* `docker rm [container_name]`: 컨테이너를 삭제. 실행 중인 컨테이너는 삭제할 수 없음
* `docker rm -f [container_name]`: 실행 중인 컨테이너도 삭제 가능
* `docker container prune`: 모든 컨테이너 삭제

### 컨테이너

#### 컨테이너 생성

`-i` 옵션으로 상호 입출력을, `-t` 옵션으로 tty를 활성화해서 배시(bash) 셸을 사용하도록 컨테이너를 설정해준다. `docker run` 명령어에서 이 두 옵션 중 하나라도 사용하지 않으면 셸을 정상적으로 사용할 수 없다. 원하는 이미지와 컨테이너 이름을 가진 컨테이너를 생성하는 방법에는 다음과 같은 방법이 있다.

* `docker run -i -t --name [container_name] [image]`

* `docker create -i -t --name [container_name] [image]`

`docker create` 명령은 `docker run` 명령어와 달리 컨테이너를 생성만할 뿐 내부로 들어가지 않는다. 보통 컨테이너를 생성함과 동시에 시작하기 때문에 `docker run` 명령어를 더 자주 사용한다.

#### 컨테이너 내부에서 빠져나오는 방법

컨테이너 내부에서 빠져나오면서 동시에 컨테이너를 정지시키는

* `exit`
* `Ctrl + D`

방법과 컨테이너를 정지하지 않고 빠져나오는

* `Ctrl + P, Q`

방법이 있다. `Ctrl + P, Q` 방법이 컨테이너의 셸에서만 빠져나오기 때문에 컨테이너 애플리케이션을 개발하는 목적으로 사용할 때 많이 쓰인다.