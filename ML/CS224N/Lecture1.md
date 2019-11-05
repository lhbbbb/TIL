# CS224N Lecture 1

## Human language

### 용어 정리

* invincible: 무적
* pathetically: 병적으로
* denotation: 표시
* thesaurus: 지식의 보고
* synonym: 동의어
* hypernym: 약어
* lexicon: 사전, 어휘

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