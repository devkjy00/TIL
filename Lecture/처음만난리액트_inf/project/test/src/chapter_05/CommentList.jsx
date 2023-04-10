import React from "react";
import Comment from "./Comment";

const comments = [
    {
        name: "kjy",
        comment: "hi, guys",
    },
    {
        name: "kjy",
        comment: "hi, guys",
    },
    {
        name: "kjy",
        comment: "hi, guys",
    }
]

function CommentList(props) {
    return (
        <div>
            {comments.map((comment) => {
                return <Comment name={comment.name} comment={comment.comment}/>
            })}
        </div>
    );
}

export default CommentList;