import React from "react";
import classNames from "classnames";

function NavbarBot(props) {

    return(
        <nav className={classNames("navbar","navbar-expand-lg", "navbar-light", "bg-light", "fixed-bottom")}>
            <div className="container">
                <ul className="navbar-nav mr-auto">
                    <li className="nav-item col-sm-5">
                        <a
                            className="nav-link"
                            href="#"
                            onClick={() => props.changePage("main")}
                        >
                            Home
                        </a>
                    </li>
                    <li className="nav-item col-sm-5">
                        <a
                            className="nav-link"
                            href="#"
                            onClick={() => props.changePage("Search")}
                        >
                            Search
                        </a>
                    </li>
                    <li className="nav-item col-sm-5">
                        <a
                            className="nav-link"
                            href="#"
                            onClick={() => props.changePage("Add")}
                        >
                            Add
                        </a>
                    </li>
                    <li className="nav-item col-sm-5">
                        <a
                            className="nav-link"
                            href="#"
                            onClick={() => props.changePage("Likes")}
                        >
                            Likes
                        </a>
                    </li>
                    <li className="nav-item col-sm-5">
                        <a
                            className="nav-link"
                            href="#"
                            onClick={() => props.changePage("Profile")}
                        >
                            Profile
                        </a>
                    </li>
                </ul>
            </div>
        </nav>
    );
}

export default NavbarBot;
