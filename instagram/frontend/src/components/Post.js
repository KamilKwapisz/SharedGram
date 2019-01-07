import React, {Component} from "react";
import {PropTypes} from "prop-types";
import StoryCircle from "./StoryCircle";
import Comment from "./Comment";
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
                    <div className = "col">
                        <StoryCircle user = {{name: this.props.user.name}} activeStory/>
                    </div>
                    <div className = "col">
                         {this.props.user.name}
                    </div>
                </div>
                <div className = "row">
                    <div className = "offset-md-2">
                        <img src = "" alt = "Post"/>
                    </div>
                </div>
                <div className = "row">
                    <div className = "offset-md-2">
                        <Comment user = {{name: this.props.user.name}} text = "Comment"/>
                    </div>
                </div>
            </div>
        )
    }
}

export default Post;
