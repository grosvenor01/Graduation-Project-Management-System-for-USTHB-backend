import bureau from '../assets/images/bureau.png';
import React from 'react';
function LoginLeft(){
    return (
        <div className='loginleft' >
            <h1>Encadrer , Commancer <br/>
            votre projet fin d’etude <br/>
            tout de suite.</h1>
            <p>
            Rejoignez notre plateforme dès aujourd'hui et <br/>
            découvrez un monde de possibilités !
            </p>
            <br />
            <img className='loginleftimg' src={bureau} alt="" />
            <span className="shadow"></span>
        </div>
    )
}

export default LoginLeft