import React, { Component } from "react";
import { hot } from "react-hot-loader";
import axios from "axios";

import "./App.css";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      currentHaiku: ""
    };
  }

  _getHaiku() {
    axios.get("http://192.168.99.100:5000/haiku").then(res => {
      this.setState({
        currentHaiku: res.data
      });
      console.log("haiku: ", res.data);
    });
  }

  render() {
    return (
      <div className="App">
        <h1> Random Poem Generator! </h1>
        <button onClick={this._getHaiku}> I want a random Haiku </button>
        <div>{this.state.currentHauku}</div>
      </div>
    );
  }
}

export default hot(module)(App);
