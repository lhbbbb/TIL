# Maximum Likelihood Estimation

이 글은 [ratsgo's blog](https://ratsgo.github.io/statistics/2017/09/23/MLE/)와 위키피디아의 내용을 정리했음을 먼저 밝힙니다.

## 개념

Likelihood는 이미 주어진 표본적 증거에 비추어 보았을 때, 모집단에 관해 어떠한 통계적 추정이 그럴듯한(Likelihood) 정도를 말해주는 것을 가리킨다. 즉, 모수가 미지의 $\theta$인 확률분포에서 뽑은 표본(관측치) $x$들을 사용하여 모수 $\theta$를 추정하는 기법이다. 우도 $L(\theta|x)$는 $\theta$가 전제되었을 때 표본 $x$가 등장할 확률인 $p(x|\theta)$에 비례한다.
$$
L(\theta|x) \propto p(x|\theta)
$$

이산 확률 변수에서는 특정 사건이 일어날 확률 = 우도(가능도)가 되며, 연속 확률 변수에서는 Likelihood가 확률이 아니라, $pdf$의 $y$값이 Likelihood가 된다. 수식적으로, 가능도라는 것은 $y=f(x)$로 표현할 수 있는 수식이다.

## 방법

어떤 모수 $\theta$로 결정되는 확률변수들의 모임 $(X_1,X_2,X_3,\dotsc,X_N)$이 있고, 이 모임의 확률밀도함수나 확률질량함수가 $f$라 할 때, 이 확률변수들에서 각각 값 $x_1, x_2, \dotsc, x_n$을 얻었을 경우, 가능도 $L(\theta)$는 다음과 같다.
$$
L(\theta) = f_\theta(x_1,x_2,\dotsc,x_n)
$$
여기에서 가능도를 최대로 만드는 $\theta$는
$$
\hat\theta = \arg\max\limits_\theta L(\theta)
$$

가 된다.

이 때 $X_1, X_2, X_3, \cdots, X_n $이 모두 독립적(독립사건은 곱연산)이고 같은 확률분포를 가지고 있다면, $L$은 다음과 같이 표현이 가능하다.
$$
L(\theta) = \prod_{i}{f_\theta(x_i)}
$$
또한, [로그함수는 단조 증가](./로그함수의성질.md)하므로, $L$에 로그를 씌운 값의 최댓값은 원래 값 $\hat\theta$와 같고, 이 경우 계산을 간단하게 할 수 있다.
$$
L^*(\theta) = logL(\theta) = \sum_ilogf_\theta(x_i)
$$
