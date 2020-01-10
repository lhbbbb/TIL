import React from 'react';
// import PropTypes from 'prop-types';

class App extends React.Component {
  state = {
    count: 0
  }
  add = () => {
    console.log("add")
    this.setState(current => ({count:current.count + 1}))
  }
  minus = () => {
    console.log("minus")
    this.setState({count:this.state.count - 1})
  }
  render() {
    return (
      <div>
        <h1>I'm a {this.state.count}</h1>
        <button onClick={this.add}>Plus</button>
        <button onClick={this.minus}>Minus</button>
      </div>
    )
  }
}

export default App;
