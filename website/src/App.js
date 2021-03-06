import React, { Component } from 'react';
import UserView from './UserView.js';
import axios from 'axios';
import ReactGA from 'react-ga';

import './App.css';

ReactGA.initialize('UA-131786508-1');

class App extends Component {

  componentDidMount() {
    this.setState({ 'users': [] });
    this.loadData('week')()
  }

  loadData(date_filter) {
    var that = this;
    return function() {
      axios.get(`http://www.thebachelorgram.com/update/?filter=` + date_filter)
        .then(res => {
          that.setState({ "users": res.data });
        });
      }
  }

  render() {

    ReactGA.pageview('/homepage');

    var users = []
    if (this.state) {
      users = this.state.users;
    }

    return (
      <div className="App">
        <h1>Bachelor Insta Followers</h1>
        <div className="date-selector">
          <a onClick={this.loadData('day')}>Day</a>
          <a onClick={this.loadData('week')}>Week</a>
          <a onClick={this.loadData('month')}>Month</a>
        </div>
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
