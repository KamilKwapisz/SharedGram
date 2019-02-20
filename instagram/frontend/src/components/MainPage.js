import React from 'react';
import ScrollView from "./ScrollView";
import PostsList from "./PostsList";

//Array passed to PostList, for testing only
const posts = [
    {name: "Pioter", likes: 10, views: 100},
    {name: "Bartosz", likes: 15, views: 500},
    {name: "Kamil", likes: 100, views: 1000}
];

function MainPage(props){

    return(
        <div>
            <ScrollView infinite>
                <PostsList posts={posts}/>
            </ScrollView>
        </div>
    );
}

export default MainPage;
