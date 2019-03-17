import React from "react";
import {NavLink} from "react-router-dom";
import classNames from "classnames";

export default function NavbarBot() {
    return(
        <div className="container">
            <nav className="nav-bot">
                <ul className="list-unstyled">
                    <div className="row justify-content-around">
                        <li className="col-xs">
                            <NavLink
                                exact
                                className="nav-link"
                                to="/"
                            >
                            Home
                            </NavLink>
                        </li>
                        <li className="col-xs">
                            <NavLink
                                exact
                                className="nav-link"
                                to="/search"
                            >
                            Search
                            </NavLink>
                        </li>
                        <li className="col-xs">
                            <NavLink
                                exact
                                className="nav-link"
                                to="/add"
                            >
                            Add
                            </NavLink>
                        </li>
                        <li className="col-xs">
                            <NavLink
                                exact
                                className="nav-link"
                                to="/likes"
                            >
                            Likes
                            </NavLink>
                        </li>
                        <li className="col-xs">
                            <NavLink
                                exact
                                className="nav-link"
                                to="/profile"
                            >
                            Profile
                            </NavLink>
                        </li>
                    </div>
                </ul>
            </nav>
        </div>
    );
}
