import React from 'react';
import ReactDOM from 'react-dom';
import Bar from './shared/Bar'
import Sidebar from './shared/Sidebar'
import App from './components/app/App';
import './assets/css/main.css';
import './assets/css/mdl2.css';
import './assets/css/sidebar.css';
import './assets/css/bar.css';
import { BrowserRouter, Route } from "react-router-dom";
 
//import * as serviceWorker from './serviceWorker';
 
const BarRoute = ({exact, path, component: Component}) => (
  <Route exact={exact} path={path} render={(props) => (
    <div>
      <Bar/>
      <Sidebar/>
      <Component {...props}/>
    </div>
  )}/>
)

ReactDOM.render(
  <React.StrictMode>
     <BrowserRouter>
        <div className="App">
          <BarRoute path="/" exact component={App} />
        </div>
      </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);
 
// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
//serviceWorker.unregister();
