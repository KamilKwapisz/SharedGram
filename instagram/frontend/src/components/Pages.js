import React, { useState } from 'react';
import NavbarBot from "./NavbarBot";
import NavbarTop from "./NavbarTop";
import ScrollView from "./ScrollView";
import PostsList from "./PostsList";

//here all the page changing will take place
function Pages(props){
    //which subpage are we on
    const[pageOn, setPageOn] = useState("main");

    return(
        <div>
            <NavbarTop changePage={setPageOn}/>
            <NavbarBot changePage={setPageOn}/>
            {/*V testing pageswitching*/}
            Current page: {pageOn}
            <ScrollView infinite>
                <PostsList posts={props.posts}/>
            </ScrollView>
        </div>
    );
}

export default Pages;
