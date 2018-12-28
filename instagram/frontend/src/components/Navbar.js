import React, {Component} from "react";
import {PropTypes} from "prop-types";
var classNames = require('classnames');

class Navbar extends Component {
    static propTypes = {
        text: PropTypes.string.isRequired,
    };


    render() {
        return <nav className={classNames("navbar","navbar-expand-lg", "navbar-light", "bg-light", {
            'fixed-top': this.props.top,
            'fixed-bottom': this.props.bottom
        })}>
            <div className="container">
                <a className="navbar-brand" href="#">{this.props.text}</a>
            </div>
        </nav>;
    }
}

export default Navbar;
