import React from 'react';
import Post from './Post';

const PostsList = props => {
    //"Each child in an array or iterator should have a unique "key" prop." Warning needs to be resolved
    const PostArray = props.posts.map((post) => {
        return (
            <Post user={post}/>
        );
    });

    return(
        <div>
            {PostArray}
        </div>
    );
};

export default PostsList;
