import React from 'react';
function Box(props){
    return(
        <div className="boxx">
            <h1 className="num">{props.num}</h1>
            <h2 className="titlenum">{props.title}</h2>
            <p className="paranum">{props.text}</p>
        </div>
    )
}

export default Box