import React, {Component} from "react";

class LikeBar extends Component{


    render(){
        return(
            <div className = "row justify-content-between">
                <div className = "col-5">
                    <div className = "row">
                        <div className = "col-2">
                            <button type="button" className="btn btn-outline-dark">Like</button>
                        </div>
                        <div className = "col-4">
                            <button type="button" className="btn btn-outline-dark">Comment</button>
                        </div>
                        <div className = "col-2">
                            <button type="button" className="btn btn-outline-dark">Share</button>
                        </div>
                    </div>
                </div>
                <div className = "col-2">
                    <button type="button" className="btn btn-outline-dark">Save</button>
                </div>
            </div>
        );
    }
}

export default LikeBar;
