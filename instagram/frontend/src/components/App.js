import React from "react";
import ReactDOM from "react-dom";
import Pages from "./Pages";

//Array passed to PostList, for testing only
const posts = [
    {name: "Pioter", likes: 10, views: 100},
    {name: "Bartosz", likes: 15, views: 500},
    {name: "Kamil", likes: 100, views: 1000}
];

const element =
    <div>
        <Pages posts={posts}/>
    </div>;

window.onload = ReactDOM.render(
    element,
    document.getElementById('app')
);
