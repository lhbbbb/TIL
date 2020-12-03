# Make movie app

앞에서 배웠던 개념들을 사용해 간단한 movie app을 만들어보도록 하겠습니다. data를 fetch하는 방법에는 `axios`를 사용하는 것과 `fetch`를 사용하는 방법이 있는데, 여기서는 `axios`를 사용하는 방법에 대해서 다루도록 하겠습니다.

## 준비

터미널에서 `npm i axios` 명령어를 통해 관련 패키지를 설치합니다.

## Movie

### Fetching Movies from API

영화 데이터를 가져오기 위해 외부 API를 사용하도록 하겠습니다. 앞에서 설치한 `axios`를 사용하여 가져옵니다. `axios`를 통해 가져오는 데이터의 양이 많아 시간이 오래 걸릴 수 있으므로 `async`, `await`를 통해 비동기 처리를 해줍니다. 비동기 처리를 해주게 되면 axios의 작업이 끝날때까지 다음 작업을 하지 않고 기다리게 됩니다.

```react
import React from "react";
import axios from "axios";

class App extends React.Component {
    state = {}
	getMovies = async() => {
        const movies = await axios.get("https://yts-proxy.now.sh/list_movies.json")
    }
    componentDidMount() {
        this.getMovies()
    }
}
```

### Rendering the Movies

Movie 컴포넌트를 생성하여 데이터를 props로 넘겨주고 유효성 검사까지 해주는 작업을 해보도록 하겠습니다. Movie 컴포넌트는 state를 사용하여 업데이트 관리를 해줄 필요가 없으므로 클래스 컴포넌트가 아닌 function 컴포넌트로 작성하였습니다.

```react
import React from "react";
import PropTypes from "prop-types";

function Movie({ id, year, title, summary, poster}) {
    return <h5>{ title }</h5>
}

Movie.propTypes = {
    id: PropTypes.number.isRequired,
    year: PropTypes.number.isRequired,
    title: PropTypes.string.isRequired,
    summary: PropTypes.string.isRequired,
    poster: PropTypes.string.isRequired
};

export default Movie;
```

```react
import React from 'react';
import axios from "axios";
import Movie from "./Movie";

class App extends React.Component {
  state = {
    isLoading: true,
    movies: []
  }
  getMovies = async () => {
    const {data: { data: { movies }}} = await axios.get("https://yts-proxy.now.sh/list_movies.json") 
    // this.setState({ movies: movies })
    this.setState({ movies, isLoading: false })
  }
  componentDidMount() {
    console.log("did mounting")
    this.getMovies();
  }
  componentDidUpdate() {
    console.log("updating")
  }
  render() {
    console.log("rendering")
    const {isLoading, movies} = this.state
    return <div>{ isLoading ?
      "Loading..."
      : movies.map(movie => {
      return <Movie id={movie.id}
      key={movie.id}
      year={movie.year}
      title={movie.title}
      summary={movie.summary}
      poster={movie.medium_cover_image}/>
    })}</div>;
  }
}

export default App;
```

### Styling the Movies

`App.css`와 `Movie.css` 와 같이 `.css` 파일을 만들고 import를 하여 클래스나 id로 특정 이름을 가진 태그들에 css를 적용시킬 수 있다. HTML 태그에서는 클래스를 쓸 때 `class` 속성을 사용하면 되지만 JSX에서는 `className`이란 속성을 사용한다.

```react
import "./App.css"
```

