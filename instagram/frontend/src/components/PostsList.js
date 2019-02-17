import React from 'react';
import Post from './Post';

const PostsList = props => {
    const PostArray = props.posts.map((post, i) => { //fixme: 'i' should be replace for some id given by DJango
        return (
            <Post post={post} key={i} />
        );
    });

    return(
        <div>
            {PostArray}
        </div>
    );
};

export default PostsList;
