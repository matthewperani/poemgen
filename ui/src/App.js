import React, { Component } from "react";
import { hot } from "react-hot-loader";
import axios from "axios";

import "./App.css";

class App extends Component {
  //componentDidMount() {
  //  axios.get('/hello')
  //  .then( res => {
  //    console.log(res.data);
  //  });
  //}

  render() {
    return (
      <div className="App">
        <h1> Random Poem Generator! </h1>
        <button> I want a random Poem </button>
      </div>
    );
  }
}

export default hot(module)(App);
