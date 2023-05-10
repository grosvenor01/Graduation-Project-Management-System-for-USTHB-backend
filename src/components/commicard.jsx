import React from 'react';
function CommiCard(){
    return (
        <div className="respocard">
        <h1>Titre de theme</h1>
        <h2>Etudiant : <small>Saidi abdelkader</small></h2> 
        <h2>Binome : <small>Tareb Selma</small></h2> 
        <h2>Encadrent : <small>Ferihi</small> </h2> 
        <h4>click <small>fiche pfe</small></h4>
        <div className="comibtn">
            <button className="cbtn1">Accepter</button>
            <button className="cbtn2">refuser</button>
        </div>
        </div>
    )
}

export default CommiCard