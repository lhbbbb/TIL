# GitDay2

## 2019.09.10

S(주어) merge O(목적어): O를 병합한다

S rebase O: 새로 base를 ~에 만든다

`git rm --cached [file_name]`: unstage file

`git rm --cached -r .`: unstage all file

`git remote add upstream https://github.com/sspy21/nhaeng.git`

https://github.com/lhbbbb/collabo/invitaions

## master / slave 협업

### slave

github에서 new pull request 버튼 => create pull request

### Flow

1. push &pull
   - 동기적처리를 해야하는 업무
   - 동시적 작업이 되지 않음
2. Branching & Pull Request
   - 현실 협업 모델
3. Fork & Pull
   - 오픈소스, 코드 컨트리뷰션



project tab에서 미니 트렐로 만들 수 있음

settings => collaborators

settings => branches

![branches](assets\branches.png)

## Tip

* [learn git branch in gui](https://learngitbranching.js.org/)

* 소프트웨어는 BFS로 가야한다.

* 오픈소스와 API 현재 소프트웨어에서 가장 중요한 요소