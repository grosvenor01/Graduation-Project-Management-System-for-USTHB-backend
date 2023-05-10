import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCheck,faUp,faDown} from '@fortawesome/free-solid-svg-icons'
import profilepic from '../assets/images/profilepic.png';
import { useState, useRef,useEffect } from 'react';
import React from 'react';
function Comment(){


    return (
        <div className="qstcomment">
            <img src={profilepic} alt="" />
            <div className="qstinput">
                <h1>Full name</h1>
                <input type="text" 
                className='commentinput' 
                placeholder='ajouter votre commentaire ...' 
                /> 
            </div>
            <div className="check">
                <FontAwesomeIcon 
                icon={faCheck} 
                className='checkicon'
                /> 
            </div>
       </div>
    )
}

export default Comment