import React from "react";
import ReactDOM from "react-dom";
//import DataProvider from "./DataProvider";
//import Table from "./Table";
function tick() {
  const element = (
    <div>
      <h1>Hej bananki i karotki!</h1>
      <h2>Jest {new Date().toLocaleTimeString()}.</h2>
    </div>
  );
  ReactDOM.render(
    element,
    document.getElementById('app')
  );
}

setInterval(tick, 1000);
