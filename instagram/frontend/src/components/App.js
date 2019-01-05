import React from "react";
import ReactDOM from "react-dom";
import StoryCircle from "./StoryCircle";
import Comment from "./Comment";
import NavbarBot from "./NavbarBot";
import NavbarTop from "./NavbarTop";
import ScrollView from "./ScrollView";

//import DataProvider from "./DataProvider";

const element = <div className="row container">
    <NavbarTop/>
    <NavbarBot/>
    <div className="container">
        <div className="row">
            <ScrollView infinite>
                <StoryCircle user={{name: "Piotr"}} activeStory/>
            </ScrollView>
        </div>
    </div>
</div>;

window.onload = ReactDOM.render(
    element,
    document.getElementById('app')
);
