import React from "react";
import classNames from "classnames";

function NavbarTop(props) {
    
    return(
        <nav className={classNames("navbar","navbar-expand-lg", "navbar-light", "bg-light", "fixed-top")}>
            <div className="container">
                <a
                    className="navbar-brand"
                    href="#"
                    onClick={() => props.changePage("main")}
                >
                    SharedGram
                </a>

                <a
                    className="navbar-text"
                    href="#"
                    onClick={() => props.changePage("message")}
                >
                    message
                </a>
            </div>
        </nav>
    );
}

export default NavbarTop;
