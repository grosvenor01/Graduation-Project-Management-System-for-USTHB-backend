import women from '../assets/images/women.png';
import { faCheck, faXmark } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import React from 'react';
function Notif (){
    return (
        <div className="notif">
             <div className="notiftop">
                <img src={women} alt="" />
                <h2>Luy Robin</h2>
                <h4>1 minute ago</h4>
             </div>
             <div className="notifbtm">
                <p id="notifcontent">
                un binome a demender de <br /> vous encadrer au theme <br /> intituler :  “ le titre de <br /> theme” 
                </p>
                <FontAwesomeIcon icon={faXmark} className='no'/> 
                <FontAwesomeIcon icon={faCheck} className='yes'/>
             </div>
        </div>
    )
}

export default Notif