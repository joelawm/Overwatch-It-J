import React from "react";
import { Link } from "react-router-dom";
 
export default class Sidebar extends React.Component {
  render() {
    return (
      <div>
        <div class="sidenav">
          <a href="/#">Dashboard</a>
          <a href="/#">Servers</a>
          <a href="/#">Reports</a>
          <a href="/#">Scripts</a>
          <a href="/#">Powerwall</a>
          <a href="/#">Account</a>
	      </div>
      </div>
    );
  }
}