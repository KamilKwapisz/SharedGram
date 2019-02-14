import React from "react";
import ReactDOM from "react-dom";
import StoryCircle from "./StoryCircle";
import Comment from "./Comment";
import NavbarBot from "./NavbarBot";
import NavbarTop from "./NavbarTop";
import ScrollView from "./ScrollView";
import PostsList from "./PostsList";

//import DataProvider from "./DataProvider";

//Array passed to PostList, for testing only
const posts = [
    {name: "Pioter", likes: 10},
    {name: "Bartosz", likes: 15},
    {name: "Kamil", likes: 100}
];


const element =
    <div className="row">
        <NavbarTop/>
        <NavbarBot/>
        <ScrollView infinite>
            <PostsList posts={posts}/>
        </ScrollView>
    </div>;

window.onload = ReactDOM.render(
    element,
    document.getElementById('app')
);
