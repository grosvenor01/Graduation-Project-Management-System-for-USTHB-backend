import profilpic from '../assets/images/profilepic.png';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPaperPlane} from '@fortawesome/free-solid-svg-icons'
import React from 'react';
function UserName(){
    return(
        <div className="username">
            <img src={profilpic} alt="" />
            <div className="usrtexts">
                <h1>Username</h1>
                <h2>grade 1</h2>
            </div>
            <div className="senddiv">
                <FontAwesomeIcon icon={faPaperPlane} className='sendicon'/>
            </div>
        </div>
    )
}

export default UserName