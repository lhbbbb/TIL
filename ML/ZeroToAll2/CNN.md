# CNN(Convolutional Neural Network)

모두의 딥러닝 시즌 2 강의를 듣고 정리한 내용임을 밝힙니다.

## 개요

이미지 인식에 사용되는 신경망이다.

Feature Extraction from Image, Classification의 2가지 step으로 구분된다. 

## 용어 정리

### Convolution

이미지 위에서 stride 값 만큼 filter(kernel)을 이동시키면서 겹쳐지는 부분의 각 원소의 값을 곱해서 모두 더한 값을 출력으로 하는 연산

### Stride and Padding

Stride: filter를 한번에 얼마나 이동할 것인가를 결정

padding: zero-padding

## Feature Extraction from Image

`Convolutional stage`, `Non-linear stage`, `Pooling stage`의 3 steps으로 구분된다.

 
