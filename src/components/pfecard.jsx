
import React from 'react';
function PfeCard({details,setPopup}) {
    return (
        <div className="pfecard">
            <h1>{details.name}</h1>
            <h3>Détails : </h3>
            <h4>{details.detail} </h4>
            <h3>Competance requits </h3>
            <div className="cmpts">
                <div className="cmpt"> {details.cmpt1}</div>
                <div className="cmpt">{details.cmpt2}</div>
                <div className="cmpt">{details.cmpt3}</div>
            </div>
            <button onClick={()=>setPopup(true)} >Modifier</button>
        </div>
    )
}

export default PfeCard