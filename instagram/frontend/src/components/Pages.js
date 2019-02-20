import React, { useState } from 'react';
import {Route, Link, Switch, BrowserRouter as Router} from 'react-router-dom';
import NavbarBot from "./NavbarBot";
import NavbarTop from "./NavbarTop";
import MainPage from "./MainPage";
import WIPPage from "./WIPPage";
import NotFoundPage from "./NotFoundPage";

//here all the page changing will take place
function Pages(props){
    //which subpage are we on
    const[pageOn, setPageOn] = useState("main");

    return(
        <Router>
            <div>
                <NavbarTop />
                <NavbarBot />
                <Switch>
                    <Route exact path="/" component={MainPage} />
                    <Route path="/message" component={WIPPage} />
                    <Route path="/search" component={WIPPage} />
                    <Route path="/add" component={WIPPage} />
                    <Route path="/likes" component={WIPPage} />
                    <Route path="/profile" component={WIPPage} />
                    <Route component={NotFoundPage} />
                </Switch>
            </div>
        </Router>
    );
}

export default Pages;
