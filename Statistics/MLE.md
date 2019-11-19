# Maximum Likelihood Estimation

이 글은 [ratsgo's blog](https://ratsgo.github.io/statistics/2017/09/23/MLE/)와 위키피디아의 내용을 정리했음을 먼저 밝힙니다.

## 개념

Likelihood는 이미 주어진 표본적 증거에 비추어 보았을 때, 모집단에 관해 어떠한 통계적 추정이 그럴듯한(Likelihood) 정도를 말해주는 것을 가리킨다. 즉, 모수가 미지의 $\theta$인 확률분포에서 뽑은 표본(관측치) $x$들을 사용하여 모수 $\theta$를 추정하는 기법이다. 우도 $L(\theta|x)$는 $\theta$가 전제되었을 때 표본 $x$가 등장할 확률인 $p(x|\theta)$에 비례한다.
$$
L(\theta|x) \propto p(x|\theta)
$$

## 방법

어떤 모수 $\theta$로 결정되는 확률변수들의 모임 $(X_1,X_2,X_3,\dotsc,X_N)$이 있고, 이 모임의 확률밀도함수나 확률질량함수가 $f$라 할 때, 이 확률변수들에서 각각 값 $x_1, x_2, \dotsc, x_n$을 얻었을 경우, 가능도 $L(\theta)$는 다음과 같다.
$$
L(\theta) = f_\theta(x_1,x_2,\dotsc,x_n)
$$
여기에서 가능도를 최대로 만드는 $\theta$는
$$
\theta
$$


