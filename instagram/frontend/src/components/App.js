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
    {name: "Pioter", likes: 10, views: 100},
    {name: "Bartosz", likes: 15, views: 500},
    {name: "Kamil", likes: 100, views: 1000}
];


const element =
    <div>
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
