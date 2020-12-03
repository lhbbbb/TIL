import React from 'react';
import axios from "axios";
import Movie from "../components/Movie";

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
    return (
      <section className="container">
          { isLoading ? ( 
            <div className="loader">
              <span className="loader_text">Loading...</span>
            </div>
          ) : (
            <div className="movies">
              {movies.map(movie => (
                <Movie id={movie.id}
                key={movie.id}
                year={movie.year}
                title={movie.title}
                summary={movie.summary}
                poster={movie.medium_cover_image}
                genres={movie.genres}
                />
              ))}
            </div>
          )} 
      </section>
    )
  }
}

export default App;