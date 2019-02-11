import React, {Component} from "react";
import {PropTypes} from "prop-types";
import StoryCircle from "./StoryCircle";
import Comment from "./Comment";
import LikeBar from "./LikeBar";
import classNames from "classnames";

class Post extends Component{
    static propTypes = {
        post: PropTypes.object.isRequired
    };

    constructor(props){
        super(props);
    }

    render(){
        return(
            <div className = "container">
                <div className = "row">
                    <div className = "col-2">
                        <StoryCircle user = {{name: this.props.post.name}} activeStory/>
                    </div>
                    <div className = "col-10">
                         {this.props.post.name}
                    </div>
                </div>
                <div className = "row">
                    <img src = "" alt = "Post"/>
                </div>
                    <LikeBar initLikes = {this.props.post.likes}/>
                <div className = "row">
                    <Comment user = {{name: this.props.post.name}} text = "Comment"/>
                </div>
            </div>
        );
    }
}

export default Post;
