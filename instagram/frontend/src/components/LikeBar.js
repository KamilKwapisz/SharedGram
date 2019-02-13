import React, { useState } from 'react';

function LikeBar(props) {
    //Like fields
    const [liked, setIfLiked] = useState(false);
    const [likes, setLikes] = useState(props.initLikes);

    //Save field
    const [saved, setIfSaved] = useState(false);

    function likeClicked() {
        setIfLiked(true);
        setLikes(likes+1);
    }

    function dislikeClicked() {
        setIfLiked(false);
        setLikes(likes-1);
    }

    function saveClicked() {
        setIfSaved(true);
    }

    function unsaveClicked() {
        setIfSaved(false);
    }

    return(
        <div>
            <div className = "row justify-content-between">
                <div className = "col-5">
                    <div className = "row">
                        <div className = "col-2">
                            {!liked && (
                                <button type="button"
                                onClick={likeClicked}
                                className="btn btn-outline-dark">
                                Like
                                </button>
                            )}

                            {liked && (
                                <button type="button"
                                onClick={dislikeClicked}
                                className="btn btn-outline-dark">
                                Dislike
                                </button>
                            )}
                        </div>
                        <div className = "col-4">
                            <button type="button"
                            className="btn btn-outline-dark">
                            Comment
                            </button>
                        </div>
                        <div className = "col-2">
                            <button type="button"
                            className="btn btn-outline-dark">
                            Share
                            </button>
                        </div>
                    </div>
                </div>
                <div className = "col-2">
                    {!saved && (
                        <button type="button"
                        onClick={saveClicked}
                        className="btn btn-outline-dark">
                        Save
                        </button>
                    )}

                    {saved && (
                        <button type="button"
                        onClick={unsaveClicked}
                        className="btn btn-outline-dark">
                        Unsave
                        </button>
                    )}
                </div>
            </div>
            <div className = "row">
                Likes: {likes}
            </div>
        </div>
    );
}

export default LikeBar;
