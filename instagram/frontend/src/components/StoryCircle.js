import React, {Component} from "react";
import {PropTypes} from "prop-types";
import classNames from "classnames";

/*
* Component that displays a profile picture in a circle and a colorful border if a user story is available
 */
class StoryCircle extends Component {
    static propTypes = {
        user: PropTypes.object.isRequired
    };

    constructor(props) {
        super(props);
        this.state = {
            activeStory: this.props.activeStory
        };
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick(){
        console.log('clicked story of ' + this.props.user.name);//testing only
        //todo: show story in a modal
        this.setState(state => (
            {activeStory: false}
        ));
    }


    render() {
        return <div className={classNames({
            'activeStory': this.state.activeStory
        })}
        onClick={this.handleClick}>
            < img
                src={this.props.user.image}
                className="rounded-circle img-fluid"
                alt={this.props.user.name}
            />
        </div>;
    }
}

export default StoryCircle;
