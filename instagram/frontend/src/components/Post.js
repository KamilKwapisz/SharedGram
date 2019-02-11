import React, {Component} from "react";
import {PropTypes} from "prop-types";
import StoryCircle from "./StoryCircle";
import Comment from "./Comment";
import LikeBar from "./LikeBar";
import classNames from "classnames";

class Post extends Component{
    static propTypes = {
        user: PropTypes.object.isRequired
    };

    constructor(props){
        super(props);
    }

    render(){
        return(
            <div className = "container">
                <div className = "row">
                    <div className = "col-2">
                        <StoryCircle user = {{name: this.props.user.name}} activeStory/>
                    </div>
                    <div className = "col-10">
                         {this.props.user.name}
                    </div>
                </div>
                <div className = "row">
                    <img src = "" alt = "Post"/>
                </div>
                    <LikeBar />
                <div className = "row">
                    <Comment user = {{name: this.props.user.name}} text = "Comment"/>
                </div>
            </div>
        );
    }
}

export default Post;
