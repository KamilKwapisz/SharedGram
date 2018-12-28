import React, {Component} from "react";
import {PropTypes} from "prop-types";
var classNames = require('classnames');

/*
* Component that displays a profile picture in a circle and a colorful border if a user story is available
 */
class ScrollView extends Component {
    constructor(props){
        super(props);
        this.handleScroll = this.handleScroll.bind(this)
    }

    handleScroll(){
        if(this.scrollBtm < 150 && this.props.infinite){
            //todo: load more
        }
    }

    render() {
        return <div className="col scrollable" onScroll={this.handleScroll()}>
            {this.props.children}
        </div>;
    }
}

export default ScrollView;
