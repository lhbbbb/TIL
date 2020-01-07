# Vue 서버 배포

## Firebase

프로젝트에서 `npm install -g firebase-tools` 명령어로 firebase 설치한다.

`firebase login` 명령어로 로그인한다. 정보제공을 묻냐는 질문에는 y,n 둘 중 아무거나 해도 상관없다.

`firebase init` 명령어로 실행하고 `Hosting`을 space 키로 선택한 후 enter를 입력

`dist`라고 입력 후 enter를 입력한다.

`npm run build` 명령어로 컴파일한다. heroku의 collectstatic과 비슷한 기능이다.

`firebase deploy` 명령어로 deploy한다.