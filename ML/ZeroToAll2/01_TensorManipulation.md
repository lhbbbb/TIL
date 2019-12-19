# Tensor Manipulation 1

이 글은 모두의 딥러닝 시즌 2 강의를 듣고 정리한 내용임을 밝힙니다

## Vector, Matrix and Tensor

### Pytorch Tensor Shape Convention

* 2D Tensor (typical simple setting)
  * $|t| = (batch size, dim)$

* 3D Tensor (typical Computer Vision)
  * $|t| = (batch size, width, height)$
* 3D Tensor (typical Natural Language Processing)
  * $|t| = (batch size, length, dim)$



## Pytorch Tensor

변수 선언을 하는 방법은 다음과 같다.

```python
# float 자료형을 가진 텐서 생성
t = torch.FloatTensor([1.,2.,3.],
                     [4.,5.,6.],
                     [7.,8.,9.])
```

텐서의 형태를 알고 싶으면 다음 명령어들을 사용한다.

```python
t.dim() # 몇 개의 차원이 있는지 // 벡터(x)면 1, 행렬(x*y)이면 2, 3차원 텐서(x*y*z)면 3
t.size() # 모양
```

