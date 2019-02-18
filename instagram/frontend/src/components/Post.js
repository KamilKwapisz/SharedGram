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
            <div className = "post">
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
                        <div className = "col">
                            <img src = "" alt = "Post"/>
                        </div>
                    </div>
                    <LikeBar initLikes = {this.props.post.likes}
                    initViews = {this.props.post.views}
                    OP = {this.props.post.name}
                    description = "some text"/>
                </div>
            </div>
        );
    }
}

export default Post;
