import React from "react";
const { remote } = window.require('electron');
 
export default class Bar extends React.Component {
  quit_current_window(){
    remote.app.quit()
  }

  minimize_current_Window(){
    remote.getCurrentWindow().minimize()
  }

  minmax_current_window(){
    const currentWindow = remote.getCurrentWindow()
    if(currentWindow.isMaximized()) 
    {
      currentWindow.unmaximize()
    } 
    else
    {
      currentWindow.maximize()
    }
  }

  render() {
    return (
      <div>
        <div class="title-bar">
      		<div class="menu-button-container">
            <button id="menu-button" class="menu-button"/>
          </div>
          <div class="app-name-container">
            <p class="bar-text">Overwatch It J</p>
          </div>
          <div class="window-controls-container">
            <button id="minimize-button" class="minimize-button mdl2-chrome-minimize" onClick={this.minimize_current_Window}/>
            <button id="min-max-button" class="min-max-button mdl2-chrome-restore" onClick={this.minmax_current_window}/>
            <button id="close-button" class="close-button mdl2-cancel" onClick={this.quit_current_window}/>
          </div>
        </div>`
      </div>
    );
  }
}