import React, { Component } from 'react';
import UserView from './UserView.js';
import axios from 'axios';

import './App.css';

class App extends Component {

  componentDidMount() {
    this.setState({ 'users': [] });
    axios.get(`http://ec2-13-57-211-196.us-west-1.compute.amazonaws.com:3000/update`)
      .then(res => {
        this.setState({ "users": res.data });
      });
  }

  render() {

    var users = []
    if (this.state) {
      users = this.state.users;
    }

    return (
      <div className="App">
        <h1>Bachelor Insta Followers</h1>
        <div className="user-container">
          {users.map(function(user, i){
            return <UserView 
              user={user}
              key={i}
            />
          })}
        </div>
      </div>
    );
  }
}

export default App;
