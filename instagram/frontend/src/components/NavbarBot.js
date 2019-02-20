import React from "react";
import {NavLink} from "react-router-dom";
import classNames from "classnames";

function NavbarBot(props) {

    return(
        <nav className={classNames("navbar","navbar-expand-lg", "navbar-light", "bg-light", "fixed-bottom")}>
            <div className="container">
                <ul className="navbar-nav mr-auto">
                    <li className="nav-item col-sm-5">
                        <NavLink
                            exact
                            className="nav-link"
                            to="/"
                        >
                        Home
                        </NavLink>
                    </li>
                    <li className="nav-item col-sm-5">
                        <NavLink
                            className="nav-link"
                            to="/search"
                        >
                        Search
                        </NavLink>
                    </li>
                    <li className="nav-item col-sm-5">
                        <NavLink
                            className="nav-link"
                            to="/add"
                        >
                        Add
                        </NavLink>
                    </li>
                    <li className="nav-item col-sm-5">
                        <NavLink
                            className="nav-link"
                            to="/likes"
                        >
                        Likes
                        </NavLink>
                    </li>
                    <li className="nav-item col-sm-5">
                        <NavLink
                            className="nav-link"
                            to="/profile"
                        >
                        Profile
                        </NavLink>
                    </li>
                </ul>
            </div>
        </nav>
    );
}

export default NavbarBot;
