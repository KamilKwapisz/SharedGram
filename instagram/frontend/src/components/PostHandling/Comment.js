import React, {Component} from "react";
import {PropTypes} from "prop-types";
import moment from 'moment';
import StoryCircle from "../StoryCircle"
import classNames from "classnames";

/*static propTypes = {
    datetime: PropTypes.any.isRequired,

};*/

class Comment extends Component {

    constructor(props){
        super(props);
        this.datetime = moment() //fixme: testing only!
        this.state = {passedTime: moment(this.datetime).fromNow()};
    }

    componentDidMount() {
        this.timeKeeper = setInterval(
            () => this.nowUpdate(),
            10000
        );
    }

    componentWillUnmount() {
        clearInterval(this.timeKeeper)
    }

    nowUpdate(){
        this.setState({
            passedTime: moment(this.datetime).fromNow()
        });
    }

    render() {
        return <div className = "container">
            <div className = "row">
                <div className = "col-2">
                    <StoryCircle user = {{name: this.props.user.name}} activeStory/>
                </div>
                <div className = "col-10">
                    <p>
                        <b>{this.props.user.name}</b>: {this.props.text}
                        <br/>
                        <span className="text-muted">{this.state.passedTime}</span>
                    </p>
                </div>
            </div>
        </div>;
    }
}

export default Comment;
