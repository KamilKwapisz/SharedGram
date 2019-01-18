import React, {Component} from "react";
import {PropTypes} from "prop-types";
import StoryCircle from "./StoryCircle"
import classNames from "classnames";

class Comment extends Component {
    /*static propTypes = {
        datetime: PropTypes.any.isRequired,

    };*/

    constructor(props){
        super(props);
        //todo: this.props.datetime to xyz minutes/hours/dates ago conversion
        this.state = {date: new Date} //fixme: testing only!
    }

    render() {
        return <div className = "container">
            <div className = "row">
                <div className = "col-2">
                    <StoryCircle user = {{name: this.props.user.name}} activeStory/>
                </div>
                <div className = "col-10">
                    <p>
                        <b>{this.props.user.name}</b>
                        {this.props.text}
                        <br/>
                        <span className="text-muted">{this.state.date.toString()}</span>
                    </p>
                </div>
            </div>
        </div>;
    }
}

export default Comment;
