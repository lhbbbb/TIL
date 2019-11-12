# CS224N 강의노트 - 1

## Introduction to Natural Language Processing

### NLP

* 인간의 언어는 의미를 전달하기 위한 특별한 시스템
* NLP의 목적은 어떤 작업을 수행하기 위해 자연어를 컴퓨터가 이해할 수 있도록 알고리즘을 디자인하는 것에 있다

### NLP tasks

* 음성처리, 의미해석, 담화처리(?)
* Level별 task 예
  * Easy: Spell Checking, Keyword Search, Finding Synonyms
  * Medium: Parsing information from websites, documents, etc
  * Hard: Machine Translation, Semantic Analysis, Coreference, Question Answering

### 단어를 표현하는 방법

* 초기 NLP는 원자 기호로 단어를 취급했음
* NLP 작업을 잘 수행하기 위해선 단어들 간의 유사점과 차이점에 대한 개념이 필요
* word vectors를 사용하면 벡터 자체에서 쉽게 이 기능을 인코딩할 수 있음

## Word Vectors

> 목적
>
> 단어 token들을 어떠한 "단어" 공간에서 점으로 표현되는 벡터들로 인코딩하는 것

### one-hot vector 표기법

* 각 단어 하나마다 하나의 차원을 가진다고 가정
* Vocubulary의 사이즈가 N이라고 하면, N만큼의 차원이 존재

$$
w^a = \begin{bmatrix}
1\\ 
0\\
\vdots \\
0
\end{bmatrix}, \cdots, 
w^{word} = \begin{bmatrix}
0\\
\vdots \\
0\\
1\\ 
\end{bmatrix}
$$

* 각 단어를 완전히 독립된 개체로서 표현할 수 있음

  

### one-hot vector의 문제점

* 벡터끼리 직교함
* 벡터의 내적이 0이기 때문에 단어끼리의 유사성을 나타낼 수 없음

$$
(w^{hotel})^Tw^{motel} = (w^{hotel})^Tw^{cat} = 0
$$

* 따라서, 단어들 사이의 관계를 인코딩하는 공간을 찾기 위해 저차원으로 사이즈를 줄여야함
* [dimension problem](/ML/DimensionProblem.md)

## SVD Based Methods

> 목적
>
> 데이터의 특이값 분해를 수행해 데이터의 차원수를 줄여 계산 효율성을 키움과 동시에 행간에 숨어있는 의미를 이끌어내고자 함

### Word-Document Matrix

* 유사성이 있는 단어가 동시에 나타난다는 사실을 이용
* word-document matrix X는 다음의 방법을 따름
  * document $j$에서 word $i$가 매번 나타날 때마다 $X_{ij}$를 1씩 올림

### Window based Co-occurrence Matrix

* word-document matrix와 동일한 로직 적용
* 다른 점은 Matrix X는 단어들의 동시발생을 저장하여 선호도 행렬이 됨
* corpus 안의 모든 단어들을 이러한 방식으로 count
* 이 방법으로 특정한 윈도우 사이즈(단어 수) 내에서 각 단어가 몇 번 나타났는지 알 수 있음

### Applying SVD to the cooccurrence matrix

* 잠재의미분석
* [참고]([https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/04/06/pcasvdlsa/](https://ratsgo.github.io/from frequency to semantics/2017/04/06/pcasvdlsa/))



## Human language

### 용어 정리

* invincible: 무적
* pathetically: 병적으로
* denotation: 표시
* thesaurus: 지식의 보고
* synonym: 동의어
* hypernym: 약어
* lexicon: 사전, 어휘
* manifestation: 표현
* coreference: 공동참조

### 컴퓨터에서 유의미를 가지는 방법

* 동의어 및 약어를 가지고 있는 WordNet 사용

### WordNet과 같은 자원의 문제점

* 미묘한 뉘앙스가 없다
  * ex) `proficient`는 특정한 구문에서만 `good`의 동의어이다
* 단어들의 새로운 의미들이 없다
  * 최신상태를 유지하는게 불가능하다
* 명사
* 새로 만들고 반영하는데 사람의 노동력이 들어간다
* 정확한 단어의 유사도를 계산할 수 없다

### Representing words as discrete symbols

* use one-hot vectors
* vector dimension = number of words in vocabulary
  * 수많은 단어들을 각각 원 핫 벡터로 표현할 수 있어야하기 때문에 단어들의 수만큼의 차원이 존재한다

#### Problem with words as discrete symbols

* 예를 들어 호텔과 모텔 벡터가 있다고 하자
* 호텔과 모텔은 유사성이 있다
* 하지만 벡터들이 직교하기 때문에 벡터들간에 자연 유사성의 개념이 없다

###  Representing words by their context

* distributional semantics
  * 비슷한 위치에서 등장하는 단어들은 비슷한 의미를 가진다
  * 근대 통계적 NLP에 있어서 가장 성공적인 아이디어 중 하나
* w가 text에서 나타날 때, 그것의 문맥은 근처에서 나타나는 단어들의 집합이다(어떤 주어진 윈도우 내에서)

### Word vectors

## Word2vec

* word vectors를 학습하기 위한 프레임워크

### Idea

* 많은 텍스트 뭉치를 가지고 있음
* fixed vocabulary 안에서 모든 단어는 벡터로 표현됨
* 