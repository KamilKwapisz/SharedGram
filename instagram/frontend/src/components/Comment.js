import React, {Component} from "react";
import {PropTypes} from "prop-types";

class Comment extends Component {
    static propTypes = {
        datetime: PropTypes.any.isRequired,

    };

    constructor(props){
        super(props);
        //todo: this.props.datetime to xyz minutes/hours/dates ago conversion
        this.props.datetime = new Date(); //fixme: testing only!
        this.state = {date: this.props.datetime}
    }

    render() {
        return <div>
            <p>
                <b>{this.props.user.name}</b>
                {this.props.text}
                <br/>
                <span className="text-muted">this.state.date.toString()</span>
            </p>
        </div>;
    }
}

export default Comment;
