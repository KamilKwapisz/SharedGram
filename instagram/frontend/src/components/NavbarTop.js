import React from "react";
import classNames from "classnames";

const NavbarTop = () => {
    return(
        <nav className={classNames("navbar","navbar-expand-lg", "navbar-light", "bg-light", "fixed-top")}>
            <div className="container">
                <a className="navbar-brand" href="#">SharedGram</a>

                <a className="navbar-text" href="#">message</a>
            </div>
        </nav>
    );
}

export default NavbarTop;
