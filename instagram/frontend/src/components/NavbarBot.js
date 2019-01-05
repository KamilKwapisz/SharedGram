import React, {Component} from "react";
import {PropTypes} from "prop-types";
import classNames from "classnames";

class NavbarBot extends Component {

    render() {
        return <nav className={classNames("navbar","navbar-expand-lg", "navbar-light", "bg-light", 'fixed-bottom')}>
            <div className="container">
                <ul className="navbar-nav mr-auto">
                    <li className="nav-item col-sm-5">
                        <a className="nav-link" href="#">Home</a>
                    </li>
                    <li className="nav-item col-sm-5">
                        <a className="nav-link" href="#">Search</a>
                    </li>
                    <li className="nav-item col-sm-5">
                        <a className="nav-link" href="#">Add</a>
                    </li>
                    <li className="nav-item col-sm-5">
                        <a className="nav-link" href="#">Likes</a>
                    </li>
                    <li className="nav-item col-sm-5">
                        <a className="nav-link" href="#">Profile</a>
                    </li>
                </ul>
            </div>
        </nav>;
    }
}

export default NavbarBot;
