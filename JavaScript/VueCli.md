# Vue Cli

## 개념

빠른 Vue.js 개발을 위해서 사용한다.

Vue 생태계에 있어서 표준 툴링 기준이 되는 것을 목적으로 한다. 다양한 빌드 도구들이 원활하게 작동하도록 하여 , 기본 틀(구성)을 만드는 것에 시간 낭비를 하지 않고 app을 만드는 것에 집중할 수 있도록 한다.

## 설치

1. git bash창에서 `npm install -g @vue/cli` 명령어를 통해 설치한다.
2. `vue --version` 명령어로 설치가 잘 되었는지 확인한다.
3. `vue create [project_name]` 으로 프로젝트 폴더를 생성한다.
4. `npm run serve` 명령어로 서버를 구동시킨다.

## 기본 설정

### VSCode Settings

#### Indentation Set

`F1` => `preference` => `open settings(Json)` 에서 다음 내용을 추가해준다.

```
"[vue]": {
	"editor.tabSize": 2
},
```

#### `console.log` 기능 on/off

`package.json ` 파일에서 `rules` 변수에 다음 내용을 추가해준다.

```
"rules": {
	"no-console": "off" // console.log 기능 사용할 수 있게 해줌. default는 사용불가
},
```