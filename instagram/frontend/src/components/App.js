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
    {name: "Pioter"},
    {name: "Bartosz"},
    {name: "Kamil"}
];


const element = <div className="row container">
    <NavbarTop/>
    <NavbarBot/>
    <div className="container">
        <div className="row">
            <div className="offset-md-3">
                <ScrollView infinite>
                    <PostsList posts={posts}/>
                </ScrollView>
            </div>
        </div>
    </div>
</div>;

window.onload = ReactDOM.render(
    element,
    document.getElementById('app')
);
