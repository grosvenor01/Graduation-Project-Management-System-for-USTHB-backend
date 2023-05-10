import usthb from '../assets/images/usthb.png';
import profilepic from '../assets/images/profilepic.png';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHouse, faMessage,faClockRotateLeft, faGear } from '@fortawesome/free-solid-svg-icons'
import React from 'react';
function RightBar({fix}) {
    return (
        <div className='sidebar'>
            <img src={usthb} alt="" />
            <h1>Menu</h1>
            <ul>
                <li className='lili' href="/home"><i className='iconli'><FontAwesomeIcon icon={faHouse} /></i>Home</li>
                <li className='lili' href= "#"><i className="iconli"><FontAwesomeIcon icon={faMessage} /> </i> Messages</li>
                <li className='lili'href="#"><i className="iconli"><FontAwesomeIcon icon={faClockRotateLeft} /></i> historique </li>
                <li className='lili' href ="/editprofp"><i className="iconli"><FontAwesomeIcon icon={faGear} /></i> Parametres </li>
            </ul>
            <h1 className='act'>Account</h1>
            <div className='prfl'>
                <img src={profilepic} alt="" />
                <div className='infoss'>
                    <h2>Username</h2>
                    <h4>L3 ACAD student</h4>
                </div>

            </div>
        </div>
    )
}

export default RightBar