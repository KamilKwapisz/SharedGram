import React from "react";
import {NavLink} from "react-router-dom";
import classNames from "classnames";

function NavbarTop(props) {

    return(
        <nav className={classNames("navbar","navbar-expand-lg", "navbar-light", "bg-light", "fixed-top")}>
            <div className="container">
                <NavLink
                    exact
                    className="navbar-brand"
                    to="/"
                >
                SharedGram
                </NavLink>

                <NavLink
                    className="navbar-text"
                    to="/message"
                >
                message
                </NavLink>
            </div>
        </nav>
    );
}

export default NavbarTop;
